<?php
    require_once dirname(__FILE__) . '/../../config.php';

    if (!isset($URL)) $URL = 'http://www.codingame.com/html/challenges/challenges.json';
    if (!isset($HOST)) $HOST = parse_url($URL, PHP_URL_HOST);
    if (!isset($RID)) $RID = -1;
    if (!isset($LANG)) $LANG = 'RU';
    if (!isset($TIMEZONE)) $TIMEZONE = 'UTC';
    if (!isset($contests)) $contests = array();

    $prefix_contest = parse_url($URL, PHP_URL_SCHEME) . '://' . parse_url($URL, PHP_URL_HOST) . '/contests/';

    $url = 'https://www.codingame.com/services/ChallengeRemoteService/findNextVisibleChallenge';
    $json = curlexec($url, "[]", array('json_output' => true));
    foreach ($json as $a) {
        if (!isset($a['publicId'])) {
            continue;
        }
        $u = 'https://www.codingame.com/services/ChallengeRemoteService/findWorldCupByPublicId';
        $j = curlexec($u, $postfields='["' . $a['publicId'] . '", null]', array('json_output' => true));
        if (!isset($j['success']) || !isset($j['success']['challenge'])) {
            continue;
        }
        $data = $j['success']['challenge'];
        $ok = true;
        foreach (array('date', 'publicId', 'title') as $key) {
            if (!isset($data[$key]) || empty($data[$key])) {
                $ok = false;
                break;
            }
        }
        if (!$ok) {
            continue;
        }
        if (isset($data['lateTimeMax'])) {
            $duration = $data['lateTimeMax'] / 60.0;
        } else {
            $duration = '00:00';
            $description = json_decode($data['descriptionJson'], true);
            if (isset($description['challengeOptions'])) {
                foreach ($description['challengeOptions'] as $options) {
                    if ($options['iconId'] == 1) {
                        $duration = $options['title'];
                        break;
                    }
                }
            }
        }
        $contests[] = array(
            'start_time' => $data['date'] / 1000,
            'duration' => $duration,
            'title' => $data['title'],
            'url' => $prefix_contest . $data['publicId'],
            'host' => $HOST,
            'rid' => $RID,
            'timezone' => $TIMEZONE,
            'key' => $data['publicId']
        );
    }

    if ($RID === -1) {
        print_r($contests);
    }
?>