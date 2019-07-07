from ssh_linux import ssh
import re
import hashlib
import time

def qytang_get_config(ip, username='chenhu', password='chinsgis02'):
    try:
        device_config_raw = ssh(ip, username, password)
        split_result = re.split(r'\r\nhostname \S+\r\n',device_config_raw)
        device_config = device_config_raw.replace(split_result[0], '').strip()
        return device_config

    except Exception:
        return

def qytang_chack_diff(ip, username='chenhu', password='chinsgis02'):
    beforce_md5 = ''
    while True:
        device_config = qytang_get_config(ip, username, password)
        m = hashlib.md5()
        m.update(device_config.encode())
        md5_value = m.hexdigest()
        print(md5_value)
        if not beforce_md5:
            beforce_md5 = md5_value
        elif beforce_md5 != md5_value:
            print('md5 value changed!')
            break
        time.sleep(5)

if __name__ == "__main__":
    print(qytang_chack_diff('10.1.1.1', username='chenhu', password='chinsgis02'))
