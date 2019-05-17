import csv
import time

from django.contrib import admin
from django.http import HttpResponse
from django.utils import timezone

from pyclist.admin import BaseModelAdmin, admin_register
from events.models import Event, Participant, JoinRequest, Team, Login


@admin_register(Event)
class EventAdmin(BaseModelAdmin):
    list_display = ['name', 'slug', 'participants_count', 'teams_count', 'registration_deadline']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name', )}

    def participants_count(self, inst):
        return inst.participant_set.count()
    participants_count.admin_order_field = 'participants_count'

    def teams_count(self, inst):
        return inst.team_set.count()
    teams_count.admin_order_field = 'teams_count'


@admin_register(Participant)
class ParticipantAdmin(BaseModelAdmin):
    search_fields = ['coder__user__username', 'first_name', 'last_name', 'email']
    list_display = [
        'coder',
        'first_name',
        'last_name',
        'email',
        'is_coach',
    ]
    list_filter = ['event', 'is_coach', 'organization', 'country']


@admin_register(JoinRequest)
class JoinRequestAdmin(BaseModelAdmin):
    list_display = ['team', 'participant', 'created']
    search_fields = ['team', 'participant']


class TeamHasLoginFilter(admin.SimpleListFilter):
    title = 'has login'
    parameter_name = 'has_login'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Yes'),
            ('no', 'No'),
        )

    def queryset(self, request, queryset):
        ids = []
        for team in queryset:
            if Login.objects.filter(team=team, stage=team.status).exists():
                ids.append(team.pk)
        if self.value() == 'yes':
            queryset = queryset.filter(pk__in=ids)
        elif self.value() == 'no':
            queryset = queryset.exclude(pk__in=ids)
        return queryset


@admin_register(Team)
class TeamAdmin(BaseModelAdmin):
    list_display = ['name', 'status', 'coach', 'participants_count', 'author']
    search_fields = ['name', 'coach__last_name']
    list_filter = [TeamHasLoginFilter, 'status', 'event']

    def participants_count(self, inst):
        return inst.participants.count()
    participants_count.admin_order_field = 'participants_count'

    def bind_login(self, request, queryset):
        skip = 0
        done = 0
        cache = {}
        for team in queryset:
            created, _ = team.attach_login(cache=cache)
            if created:
                done += 1
            else:
                skip += 1
        self.message_user(request, '{} successfully created logins, {} skipped.'.format(done, skip))
    bind_login.short_description = 'Bind login with current status as stage'

    def import_to_csv(self, request, queryset):
        filename = 'information-{}.csv'.format(timezone.now().strftime('%Y%m%d%H%M'))
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        writer = csv.writer(response)
        writer.writerow([s.replace('_', ' ').title() for s in [
            'title',
            'first_name',
            'last_name',
            'first_name_native',
            'last_name_native',
            'middle_name_native',
            'email',
            'phone_number',
            'organization',
            'country',
            'tshirt',
            'is_coach',
        ]])
        for team in queryset:
            for m in team.members:
                writer.writerow([s.encode('utf8') for s in [
                    team.title,
                    m.first_name,
                    m.last_name,
                    m.first_name_native,
                    m.last_name_native,
                    m.middle_name_native,
                    m.email,
                    str(m.phone_number),
                    m.organization.name_ru if m.organization else '-',
                    m.country.name,
                    m.tshirt_size_value,
                    str(m.is_coach),
                ]])
        return response
    import_to_csv.short_description = 'Import to csv'

    actions = [bind_login, import_to_csv]


@admin_register(Login)
class LoginAdmin(BaseModelAdmin):
    list_display = ['team', 'stage', 'username', 'is_sent']
    search_fields = ['team__name', 'username', 'stage']
    list_filter = ['stage', 'is_sent', 'team__event']

    def get_renaming_data(self, request, queryset):
        response = HttpResponse(content_type='text')
        response['Content-Disposition'] = 'attachment; filename=namming.txt'
        for login in queryset:
            response.write('{} {}\n'.format(login.username, login.team.title))
        return response
    get_renaming_data.short_description = 'Get raw data for renameing teams'

    def get_passwords(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=passwords.csv'
        for login in queryset:
            response.write('{},{},{}\n'.format(login.username, login.password, login.team.title))
        return response
    get_passwords.short_description = 'Get passwords'

    def send_email(self, request, queryset):
        n_attempet = 5
        time_wait_on_failed = 10

        cache = {}

        skip = 0
        done = 0
        failed = 0
        for login in queryset:
            if login.is_sent:
                skip += 1
                continue
            event = login.team.event
            if event.pk not in cache:
                cache[event.pk] = event.email_backend().__enter__()

            for i in range(n_attempet):
                if login.send_email(connection=cache[event.pk]):
                    done += 1
                    time.sleep(2)
                    break
                time.sleep(time_wait_on_failed)
            else:
                failed += 1

        for connection in list(cache.values()):
            connection.close()

        self.message_user(request, '{} successfully send emails, {} skipped, {} failed.'.format(done, skip, failed))
    send_email.short_description = 'Send email with template message by stage'

    actions = [send_email, get_renaming_data, get_passwords]