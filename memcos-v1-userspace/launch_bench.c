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

  if (argc < 2) {
    printf("Usage ./launch_bench [BENCHMARK]");
    memcos_end(-1);
    return 0;
  }

  pid = fork();
  if (pid == 0) {
    execvp(argv[1], &argv[1]);
    perror("Fails to run bench");
    exit(-1);
  }
#ifdef __NOPID
  memcos_start(-1, 0);
#else
  memcos_start(pid, 0);
#endif
  printf("pid: %d\n", pid);
  waitpid(pid, &state, 0);

  memcos_end(-1);

  return 0;
}
