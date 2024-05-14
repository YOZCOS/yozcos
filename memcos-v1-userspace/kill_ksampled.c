#include <err.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int syscall_memcos_start = 449;
int syscall_memcos_end = 450;

long memcos_start(pid_t pid, int node) {
  return syscall(syscall_memcos_start, pid, node);
}

long memcos_end(pid_t pid) { return syscall(syscall_memcos_end, pid); }

int main(int argc, char **argv) {
  pid_t pid;
  int state;

  memcos_end(-1);
  return 0;
}
