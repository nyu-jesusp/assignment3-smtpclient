from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    # print(recv) #You can use these print statement to validate return codes from the server.
    # if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom = 'MAIL FROM: <>\r\n'
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    # print(recv2)
    # if recv2[:3] != '250':
    #     print('250 reply acknowledging sender not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    RCPTTO = 'RCPT TO: <>\r\n'
    clientSocket.send(RCPTTO.encode())
    recv3 = clientSocket.recv(1024).decode()
    # print(recv3)
    # if recv3[:3] != '250':
    #     print('250 reply acknowledging recipient not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    DATA = 'DATA\r\n'
    clientSocket.send(DATA.encode())
    recv4 = clientSocket.recv(1024).decode()
    # print(recv4)
    # if recv4[:3] != '354':
    #     print('354 reply to start sending data not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    # date = 'DATE: 2/25/2025\r\n'
    # clientSocket.send(date.encode())
    # subject = 'Subject: TESTing Message\r\n'
    # clientSocket.send(subject.encode())
    # message = 'This is a test message\r\n'
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start

    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    # print(recv5)
    # if recv5[:3] != '250':
    #     print('250 reply acknowledging end with . not received from server.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCmd = 'QUIT\r\n'
    clientSocket.send(quitCmd.encode())
    recv6 = clientSocket.recv(1024).decode()
    # print(recv6)
    # if recv6[:3] != '221':
    #     print('221 reply to quit not received from server.')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')