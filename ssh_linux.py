import paramiko

def ssh(ip, username, password, port=22, cmd='show ip inter bri'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command('show ip inter bri')
    x = stdout.read().decode()
    return x


if __name__ == '__main__':
    print(ssh('10.1.1.1', 'chenhu', 'chinsgis02', cmd='pwd'))
