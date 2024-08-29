This is a simple machine vision camera emulation application.
The application establishes a tcp connection with the client, and sends each line from the downloaded txt file.
The application is configured by settings.json file.

Application interface:

![image](https://github.com/user-attachments/assets/61d8c645-eac7-4da2-a293-63982da31fa0)

A simple test:
1. Start app
2. Download txt file in app
3. In windows cmd execute command: telnet camera_host camera_port (most likely, you will need to enable the telnet component in windows)
4. Touch start button


