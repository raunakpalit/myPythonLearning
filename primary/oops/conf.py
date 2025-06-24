from confetti import Config
from test_lib.test_fixtures.ecu import ecu_config
from test_lib.test_fixtures.vsa_fixture import vsa_config
from test_lib.test_fixtures.ecg_collect_payload import collect_payload_config

__all__ = ["config"]

config = Config(
    {
        'ecg': {
            'ip': '10.1.0.1',
            'username': 'root',
            'key_filename': '~/.ssh/id_ecg,~/.ssh/id_ecg_ecdsa',
            'ap_port': 'COM102',
            'token_folder': 'C:/Tools/tokens',
            'token_required': False,
            'token_list': [
                'analytics_override', 'ecg_ap_dev_sign', 'ecg_ap_dev_unsign',
                'ecg_ap_logging', 'ecg_ap_gen_debug', 'ecg_cp_debug'
            ],
            'type': 'ecg1',
        },

        'can': {
            'HS1': {
                'serial': 'V21064',
                'channel': 1,
                'bitrate': 500000,
            },
            'FD1': {
                'serial': 'V21064',
                'channel': 1,
                'bitrate': 500000,
            },
        },

        'ecg_apps': {
            'ecg_release_ex': 1.6,
        },

        'dbc': {
            'CX727': {
                'V26': 'CAN_CX727_BEV_MY21_DCV_V26',
                'MY22': {
                    'V02': 'CAN_CX727_BEV_MY22_DCV_V02',
                }
            },
        },
        'sdn_ip': '127.0.0.1',
        'ecg_ip': '10.1.0.1',
        'ecg_tcu_ip': '10.1.0.2',
        'ecg_sync_ip': '10.1.0.3',
        'port': 1883,
        'keepalive': 3600,
    })

config.extend(vsa_config)
config.extend(ecu_config)
config.extend(collect_payload_config)
ecu_config.get_config('ecu_type').set_value('ECG')
config.get_config('vsa.dbc_base_dir').set_value('FNV2_CMDB')
config.get_config('vsa.required_bus').set_value('HS1,FD1')
config.get_config('vsa.vsa_type').set_value('can_ecg')

