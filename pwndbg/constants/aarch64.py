from .constant import Constant
__NR_io_setup = Constant('__NR_io_setup',0)
__NR_io_destroy = Constant('__NR_io_destroy',1)
__NR_io_submit = Constant('__NR_io_submit',2)
__NR_io_cancel = Constant('__NR_io_cancel',3)
__NR_io_getevents = Constant('__NR_io_getevents',4)
__NR_setxattr = Constant('__NR_setxattr',5)
__NR_lsetxattr = Constant('__NR_lsetxattr',6)
__NR_fsetxattr = Constant('__NR_fsetxattr',7)
__NR_getxattr = Constant('__NR_getxattr',8)
__NR_lgetxattr = Constant('__NR_lgetxattr',9)
__NR_fgetxattr = Constant('__NR_fgetxattr',10)
__NR_listxattr = Constant('__NR_listxattr',11)
__NR_llistxattr = Constant('__NR_llistxattr',12)
__NR_flistxattr = Constant('__NR_flistxattr',13)
__NR_removexattr = Constant('__NR_removexattr',14)
__NR_lremovexattr = Constant('__NR_lremovexattr',15)
__NR_fremovexattr = Constant('__NR_fremovexattr',16)
__NR_getcwd = Constant('__NR_getcwd',17)
__NR_lookup_dcookie = Constant('__NR_lookup_dcookie',18)
__NR_eventfd2 = Constant('__NR_eventfd2',19)
__NR_epoll_create1 = Constant('__NR_epoll_create1',20)
__NR_epoll_ctl = Constant('__NR_epoll_ctl',21)
__NR_epoll_pwait = Constant('__NR_epoll_pwait',22)
__NR_dup = Constant('__NR_dup',23)
__NR_dup3 = Constant('__NR_dup3',24)
__NR_fcntl = Constant('__NR_fcntl',25)
__NR_inotify_init1 = Constant('__NR_inotify_init1',26)
__NR_inotify_add_watch = Constant('__NR_inotify_add_watch',27)
__NR_inotify_rm_watch = Constant('__NR_inotify_rm_watch',28)
__NR_ioctl = Constant('__NR_ioctl',29)
__NR_ioprio_set = Constant('__NR_ioprio_set',30)
__NR_ioprio_get = Constant('__NR_ioprio_get',31)
__NR_flock = Constant('__NR_flock',32)
__NR_mknodat = Constant('__NR_mknodat',33)
__NR_mkdirat = Constant('__NR_mkdirat',34)
__NR_unlinkat = Constant('__NR_unlinkat',35)
__NR_symlinkat = Constant('__NR_symlinkat',36)
__NR_linkat = Constant('__NR_linkat',37)
__NR_renameat = Constant('__NR_renameat',38)
__NR_umount2 = Constant('__NR_umount2',39)
__NR_mount = Constant('__NR_mount',40)
__NR_pivot_root = Constant('__NR_pivot_root',41)
__NR_nfsservctl = Constant('__NR_nfsservctl',42)
__NR_statfs = Constant('__NR_statfs',43)
__NR_fstatfs = Constant('__NR_fstatfs',44)
__NR_truncate = Constant('__NR_truncate',45)
__NR_ftruncate = Constant('__NR_ftruncate',46)
__NR_fallocate = Constant('__NR_fallocate',47)
__NR_faccessat = Constant('__NR_faccessat',48)
__NR_chdir = Constant('__NR_chdir',49)
__NR_fchdir = Constant('__NR_fchdir',50)
__NR_chroot = Constant('__NR_chroot',51)
__NR_fchmod = Constant('__NR_fchmod',52)
__NR_fchmodat = Constant('__NR_fchmodat',53)
__NR_fchownat = Constant('__NR_fchownat',54)
__NR_fchown = Constant('__NR_fchown',55)
__NR_openat = Constant('__NR_openat',56)
__NR_close = Constant('__NR_close',57)
__NR_vhangup = Constant('__NR_vhangup',58)
__NR_pipe2 = Constant('__NR_pipe2',59)
__NR_quotactl = Constant('__NR_quotactl',60)
__NR_getdents64 = Constant('__NR_getdents64',61)
__NR_lseek = Constant('__NR_lseek',62)
__NR_read = Constant('__NR_read',63)
__NR_write = Constant('__NR_write',64)
__NR_readv = Constant('__NR_readv',65)
__NR_writev = Constant('__NR_writev',66)
__NR_pread64 = Constant('__NR_pread64',67)
__NR_pwrite64 = Constant('__NR_pwrite64',68)
__NR_preadv = Constant('__NR_preadv',69)
__NR_pwritev = Constant('__NR_pwritev',70)
__NR_sendfile = Constant('__NR_sendfile',71)
__NR_pselect6 = Constant('__NR_pselect6',72)
__NR_ppoll = Constant('__NR_ppoll',73)
__NR_signalfd4 = Constant('__NR_signalfd4',74)
__NR_vmsplice = Constant('__NR_vmsplice',75)
__NR_splice = Constant('__NR_splice',76)
__NR_tee = Constant('__NR_tee',77)
__NR_readlinkat = Constant('__NR_readlinkat',78)
__NR_fstatat64 = Constant('__NR_fstatat64',79)
__NR_fstat = Constant('__NR_fstat',80)
__NR_sync = Constant('__NR_sync',81)
__NR_fsync = Constant('__NR_fsync',82)
__NR_fdatasync = Constant('__NR_fdatasync',83)
__NR_sync_file_range2 = Constant('__NR_sync_file_range2',84)
__NR_timerfd_create = Constant('__NR_timerfd_create',85)
__NR_timerfd_settime = Constant('__NR_timerfd_settime',86)
__NR_timerfd_gettime = Constant('__NR_timerfd_gettime',87)
__NR_utimensat = Constant('__NR_utimensat',88)
__NR_acct = Constant('__NR_acct',89)
__NR_capget = Constant('__NR_capget',90)
__NR_capset = Constant('__NR_capset',91)
__NR_personality = Constant('__NR_personality',92)
__NR_exit = Constant('__NR_exit',93)
__NR_exit_group = Constant('__NR_exit_group',94)
__NR_waitid = Constant('__NR_waitid',95)
__NR_set_tid_address = Constant('__NR_set_tid_address',96)
__NR_unshare = Constant('__NR_unshare',97)
__NR_futex = Constant('__NR_futex',98)
__NR_set_robust_list = Constant('__NR_set_robust_list',99)
__NR_get_robust_list = Constant('__NR_get_robust_list',100)
__NR_nanosleep = Constant('__NR_nanosleep',101)
__NR_getitimer = Constant('__NR_getitimer',102)
__NR_setitimer = Constant('__NR_setitimer',103)
__NR_kexec_load = Constant('__NR_kexec_load',104)
__NR_init_module = Constant('__NR_init_module',105)
__NR_delete_module = Constant('__NR_delete_module',106)
__NR_timer_create = Constant('__NR_timer_create',107)
__NR_timer_gettime = Constant('__NR_timer_gettime',108)
__NR_timer_getoverrun = Constant('__NR_timer_getoverrun',109)
__NR_timer_settime = Constant('__NR_timer_settime',110)
__NR_timer_delete = Constant('__NR_timer_delete',111)
__NR_clock_settime = Constant('__NR_clock_settime',112)
__NR_clock_gettime = Constant('__NR_clock_gettime',113)
__NR_clock_getres = Constant('__NR_clock_getres',114)
__NR_clock_nanosleep = Constant('__NR_clock_nanosleep',115)
__NR_syslog = Constant('__NR_syslog',116)
__NR_ptrace = Constant('__NR_ptrace',117)
__NR_sched_setparam = Constant('__NR_sched_setparam',118)
__NR_sched_setscheduler = Constant('__NR_sched_setscheduler',119)
__NR_sched_getscheduler = Constant('__NR_sched_getscheduler',120)
__NR_sched_getparam = Constant('__NR_sched_getparam',121)
__NR_sched_setaffinity = Constant('__NR_sched_setaffinity',122)
__NR_sched_getaffinity = Constant('__NR_sched_getaffinity',123)
__NR_sched_yield = Constant('__NR_sched_yield',124)
__NR_sched_get_priority_max = Constant('__NR_sched_get_priority_max',125)
__NR_sched_get_priority_min = Constant('__NR_sched_get_priority_min',126)
__NR_sched_rr_get_interval = Constant('__NR_sched_rr_get_interval',127)
__NR_restart_syscall = Constant('__NR_restart_syscall',128)
__NR_kill = Constant('__NR_kill',129)
__NR_tkill = Constant('__NR_tkill',130)
__NR_tgkill = Constant('__NR_tgkill',131)
__NR_sigaltstack = Constant('__NR_sigaltstack',132)
__NR_rt_sigsuspend = Constant('__NR_rt_sigsuspend',133)
__NR_rt_sigaction = Constant('__NR_rt_sigaction',134)
__NR_rt_sigprocmask = Constant('__NR_rt_sigprocmask',135)
__NR_rt_sigpending = Constant('__NR_rt_sigpending',136)
__NR_rt_sigtimedwait = Constant('__NR_rt_sigtimedwait',137)
__NR_rt_sigqueueinfo = Constant('__NR_rt_sigqueueinfo',138)
__NR_rt_sigreturn = Constant('__NR_rt_sigreturn',139)
__NR_setpriority = Constant('__NR_setpriority',140)
__NR_getpriority = Constant('__NR_getpriority',141)
__NR_reboot = Constant('__NR_reboot',142)
__NR_setregid = Constant('__NR_setregid',143)
__NR_setgid = Constant('__NR_setgid',144)
__NR_setreuid = Constant('__NR_setreuid',145)
__NR_setuid = Constant('__NR_setuid',146)
__NR_setresuid = Constant('__NR_setresuid',147)
__NR_getresuid = Constant('__NR_getresuid',148)
__NR_setresgid = Constant('__NR_setresgid',149)
__NR_getresgid = Constant('__NR_getresgid',150)
__NR_setfsuid = Constant('__NR_setfsuid',151)
__NR_setfsgid = Constant('__NR_setfsgid',152)
__NR_times = Constant('__NR_times',153)
__NR_setpgid = Constant('__NR_setpgid',154)
__NR_getpgid = Constant('__NR_getpgid',155)
__NR_getsid = Constant('__NR_getsid',156)
__NR_setsid = Constant('__NR_setsid',157)
__NR_getgroups = Constant('__NR_getgroups',158)
__NR_setgroups = Constant('__NR_setgroups',159)
__NR_uname = Constant('__NR_uname',160)
__NR_sethostname = Constant('__NR_sethostname',161)
__NR_setdomainname = Constant('__NR_setdomainname',162)
__NR_getrlimit = Constant('__NR_getrlimit',163)
__NR_setrlimit = Constant('__NR_setrlimit',164)
__NR_getrusage = Constant('__NR_getrusage',165)
__NR_umask = Constant('__NR_umask',166)
__NR_prctl = Constant('__NR_prctl',167)
__NR_getcpu = Constant('__NR_getcpu',168)
__NR_gettimeofday = Constant('__NR_gettimeofday',169)
__NR_settimeofday = Constant('__NR_settimeofday',170)
__NR_adjtimex = Constant('__NR_adjtimex',171)
__NR_getpid = Constant('__NR_getpid',172)
__NR_getppid = Constant('__NR_getppid',173)
__NR_getuid = Constant('__NR_getuid',174)
__NR_geteuid = Constant('__NR_geteuid',175)
__NR_getgid = Constant('__NR_getgid',176)
__NR_getegid = Constant('__NR_getegid',177)
__NR_gettid = Constant('__NR_gettid',178)
__NR_sysinfo = Constant('__NR_sysinfo',179)
__NR_mq_open = Constant('__NR_mq_open',180)
__NR_mq_unlink = Constant('__NR_mq_unlink',181)
__NR_mq_timedsend = Constant('__NR_mq_timedsend',182)
__NR_mq_timedreceive = Constant('__NR_mq_timedreceive',183)
__NR_mq_notify = Constant('__NR_mq_notify',184)
__NR_mq_getsetattr = Constant('__NR_mq_getsetattr',185)
__NR_msgget = Constant('__NR_msgget',186)
__NR_msgctl = Constant('__NR_msgctl',187)
__NR_msgrcv = Constant('__NR_msgrcv',188)
__NR_msgsnd = Constant('__NR_msgsnd',189)
__NR_semget = Constant('__NR_semget',190)
__NR_semctl = Constant('__NR_semctl',191)
__NR_semtimedop = Constant('__NR_semtimedop',192)
__NR_semop = Constant('__NR_semop',193)
__NR_shmget = Constant('__NR_shmget',194)
__NR_shmctl = Constant('__NR_shmctl',195)
__NR_shmat = Constant('__NR_shmat',196)
__NR_shmdt = Constant('__NR_shmdt',197)
__NR_socket = Constant('__NR_socket',198)
__NR_socketpair = Constant('__NR_socketpair',199)
__NR_bind = Constant('__NR_bind',200)
__NR_listen = Constant('__NR_listen',201)
__NR_accept = Constant('__NR_accept',202)
__NR_connect = Constant('__NR_connect',203)
__NR_getsockname = Constant('__NR_getsockname',204)
__NR_getpeername = Constant('__NR_getpeername',205)
__NR_sendto = Constant('__NR_sendto',206)
__NR_recvfrom = Constant('__NR_recvfrom',207)
__NR_setsockopt = Constant('__NR_setsockopt',208)
__NR_getsockopt = Constant('__NR_getsockopt',209)
__NR_shutdown = Constant('__NR_shutdown',210)
__NR_sendmsg = Constant('__NR_sendmsg',211)
__NR_recvmsg = Constant('__NR_recvmsg',212)
__NR_readahead = Constant('__NR_readahead',213)
__NR_brk = Constant('__NR_brk',214)
__NR_munmap = Constant('__NR_munmap',215)
__NR_mremap = Constant('__NR_mremap',216)
__NR_add_key = Constant('__NR_add_key',217)
__NR_request_key = Constant('__NR_request_key',218)
__NR_keyctl = Constant('__NR_keyctl',219)
__NR_clone = Constant('__NR_clone',220)
__NR_execve = Constant('__NR_execve',221)
__NR_mmap = Constant('__NR_mmap',222)
__NR_fadvise64 = Constant('__NR_fadvise64',223)
__NR_swapon = Constant('__NR_swapon',224)
__NR_swapoff = Constant('__NR_swapoff',225)
__NR_mprotect = Constant('__NR_mprotect',226)
__NR_msync = Constant('__NR_msync',227)
__NR_mlock = Constant('__NR_mlock',228)
__NR_munlock = Constant('__NR_munlock',229)
__NR_mlockall = Constant('__NR_mlockall',230)
__NR_munlockall = Constant('__NR_munlockall',231)
__NR_mincore = Constant('__NR_mincore',232)
__NR_madvise = Constant('__NR_madvise',233)
__NR_remap_file_pages = Constant('__NR_remap_file_pages',234)
__NR_mbind = Constant('__NR_mbind',235)
__NR_get_mempolicy = Constant('__NR_get_mempolicy',236)
__NR_set_mempolicy = Constant('__NR_set_mempolicy',237)
__NR_migrate_pages = Constant('__NR_migrate_pages',238)
__NR_move_pages = Constant('__NR_move_pages',239)
__NR_rt_tgsigqueueinfo = Constant('__NR_rt_tgsigqueueinfo',240)
__NR_perf_event_open = Constant('__NR_perf_event_open',241)
__NR_accept4 = Constant('__NR_accept4',242)
__NR_recvmmsg = Constant('__NR_recvmmsg',243)
__NR_arch_specific_syscall = Constant('__NR_arch_specific_syscall',244)
__NR_wait4 = Constant('__NR_wait4',260)
__NR_prlimit64 = Constant('__NR_prlimit64',261)
__NR_fanotify_init = Constant('__NR_fanotify_init',262)
__NR_fanotify_mark = Constant('__NR_fanotify_mark',263)
__NR_name_to_handle_at = Constant('__NR_name_to_handle_at',264)
__NR_open_by_handle_at = Constant('__NR_open_by_handle_at',265)
__NR_clock_adjtime = Constant('__NR_clock_adjtime',266)
__NR_syncfs = Constant('__NR_syncfs',267)
__NR_setns = Constant('__NR_setns',268)
__NR_sendmmsg = Constant('__NR_sendmmsg',269)
__NR_process_vm_readv = Constant('__NR_process_vm_readv',270)
__NR_process_vm_writev = Constant('__NR_process_vm_writev',271)
__NR_kcmp = Constant('__NR_kcmp',272)
__NR_finit_module = Constant('__NR_finit_module',273)
__NR_open = Constant('__NR_open',1024)
__NR_link = Constant('__NR_link',1025)
__NR_unlink = Constant('__NR_unlink',1026)
__NR_mknod = Constant('__NR_mknod',1027)
__NR_chmod = Constant('__NR_chmod',1028)
__NR_chown = Constant('__NR_chown',1029)
__NR_mkdir = Constant('__NR_mkdir',1030)
__NR_rmdir = Constant('__NR_rmdir',1031)
__NR_lchown = Constant('__NR_lchown',1032)
__NR_access = Constant('__NR_access',1033)
__NR_rename = Constant('__NR_rename',1034)
__NR_readlink = Constant('__NR_readlink',1035)
__NR_symlink = Constant('__NR_symlink',1036)
__NR_utimes = Constant('__NR_utimes',1037)
__NR_stat = Constant('__NR_stat',1038)
__NR_lstat = Constant('__NR_lstat',1039)
__NR_pipe = Constant('__NR_pipe',1040)
__NR_dup2 = Constant('__NR_dup2',1041)
__NR_epoll_create = Constant('__NR_epoll_create',1042)
__NR_inotify_init = Constant('__NR_inotify_init',1043)
__NR_eventfd = Constant('__NR_eventfd',1044)
__NR_signalfd = Constant('__NR_signalfd',1045)
__NR_sendfile64 = Constant('__NR_sendfile64',1046)
__NR_ftruncate64 = Constant('__NR_ftruncate64',1047)
__NR_truncate64 = Constant('__NR_truncate64',1048)
__NR_stat64 = Constant('__NR_stat64',1049)
__NR_lstat64 = Constant('__NR_lstat64',1050)
__NR_fstat64 = Constant('__NR_fstat64',1051)
__NR_fcntl64 = Constant('__NR_fcntl64',1052)
__NR_newfstatat = Constant('__NR_newfstatat',1054)
__NR_fstatfs64 = Constant('__NR_fstatfs64',1055)
__NR_statfs64 = Constant('__NR_statfs64',1056)
__NR_lseek64 = Constant('__NR_lseek64',1057)
__NR_mmap64 = Constant('__NR_mmap64',1058)
__NR_alarm = Constant('__NR_alarm',1059)
__NR_getpgrp = Constant('__NR_getpgrp',1060)
__NR_pause = Constant('__NR_pause',1061)
__NR_time = Constant('__NR_time',1062)
__NR_utime = Constant('__NR_utime',1063)
__NR_creat = Constant('__NR_creat',1064)
__NR_getdents = Constant('__NR_getdents',1065)
__NR_futimesat = Constant('__NR_futimesat',1066)
__NR_select = Constant('__NR_select',1067)
__NR_poll = Constant('__NR_poll',1068)
__NR_epoll_wait = Constant('__NR_epoll_wait',1069)
__NR_ustat = Constant('__NR_ustat',1070)
__NR_vfork = Constant('__NR_vfork',1071)
__NR_oldwait4 = Constant('__NR_oldwait4',1072)
__NR_recv = Constant('__NR_recv',1073)
__NR_send = Constant('__NR_send',1074)
__NR_bdflush = Constant('__NR_bdflush',1075)
__NR_umount = Constant('__NR_umount',1076)
__NR_uselib = Constant('__NR_uselib',1077)
__NR__sysctl = Constant('__NR__sysctl',1078)
__NR_fork = Constant('__NR_fork',1079)
__NR_syscalls = Constant('__NR_syscalls',(1079+1))
__NR_sigreturn = Constant('__NR_sigreturn',1999)
__SYS_NERR = Constant('__SYS_NERR',((129) + 1))
_SYS_TIME_H = Constant('_SYS_TIME_H',1)
SYS_accept = Constant('SYS_accept',202)
SYS_accept4 = Constant('SYS_accept4',242)
SYS_access = Constant('SYS_access',1033)
SYS_acct = Constant('SYS_acct',89)
SYS_add_key = Constant('SYS_add_key',217)
SYS_adjtimex = Constant('SYS_adjtimex',171)
SYS_alarm = Constant('SYS_alarm',1059)
SYS_bdflush = Constant('SYS_bdflush',1075)
SYS_bind = Constant('SYS_bind',200)
SYS_brk = Constant('SYS_brk',214)
SYS_capget = Constant('SYS_capget',90)
SYS_capset = Constant('SYS_capset',91)
SYS_chdir = Constant('SYS_chdir',49)
SYS_chmod = Constant('SYS_chmod',1028)
SYS_chown = Constant('SYS_chown',1029)
SYS_chroot = Constant('SYS_chroot',51)
SYS_clock_getres = Constant('SYS_clock_getres',114)
SYS_clock_gettime = Constant('SYS_clock_gettime',113)
SYS_clock_nanosleep = Constant('SYS_clock_nanosleep',115)
SYS_clock_settime = Constant('SYS_clock_settime',112)
SYS_clone = Constant('SYS_clone',220)
SYS_close = Constant('SYS_close',57)
SYS_connect = Constant('SYS_connect',203)
SYS_creat = Constant('SYS_creat',1064)
SYS_delete_module = Constant('SYS_delete_module',106)
SYS_dup = Constant('SYS_dup',23)
SYS_dup2 = Constant('SYS_dup2',1041)
SYS_dup3 = Constant('SYS_dup3',24)
SYS_epoll_create = Constant('SYS_epoll_create',1042)
SYS_epoll_create1 = Constant('SYS_epoll_create1',20)
SYS_epoll_ctl = Constant('SYS_epoll_ctl',21)
SYS_epoll_pwait = Constant('SYS_epoll_pwait',22)
SYS_epoll_wait = Constant('SYS_epoll_wait',1069)
SYS_eventfd = Constant('SYS_eventfd',1044)
SYS_eventfd2 = Constant('SYS_eventfd2',19)
SYS_execve = Constant('SYS_execve',221)
SYS_exit = Constant('SYS_exit',93)
SYS_exit_group = Constant('SYS_exit_group',94)
SYS_faccessat = Constant('SYS_faccessat',48)
SYS_fadvise64 = Constant('SYS_fadvise64',223)
SYS_fallocate = Constant('SYS_fallocate',47)
SYS_fanotify_init = Constant('SYS_fanotify_init',262)
SYS_fanotify_mark = Constant('SYS_fanotify_mark',263)
SYS_fchdir = Constant('SYS_fchdir',50)
SYS_fchmod = Constant('SYS_fchmod',52)
SYS_fchmodat = Constant('SYS_fchmodat',53)
SYS_fchown = Constant('SYS_fchown',55)
SYS_fchownat = Constant('SYS_fchownat',54)
SYS_fcntl = Constant('SYS_fcntl',25)
SYS_fcntl64 = Constant('SYS_fcntl64',1052)
SYS_fdatasync = Constant('SYS_fdatasync',83)
SYS_fgetxattr = Constant('SYS_fgetxattr',10)
SYS_flistxattr = Constant('SYS_flistxattr',13)
SYS_flock = Constant('SYS_flock',32)
SYS_fork = Constant('SYS_fork',1079)
SYS_fremovexattr = Constant('SYS_fremovexattr',16)
SYS_fsetxattr = Constant('SYS_fsetxattr',7)
SYS_fstat = Constant('SYS_fstat',80)
SYS_fstat64 = Constant('SYS_fstat64',1051)
SYS_fstatat64 = Constant('SYS_fstatat64',79)
SYS_fstatfs = Constant('SYS_fstatfs',44)
SYS_fstatfs64 = Constant('SYS_fstatfs64',1055)
SYS_fsync = Constant('SYS_fsync',82)
SYS_ftruncate = Constant('SYS_ftruncate',46)
SYS_ftruncate64 = Constant('SYS_ftruncate64',1047)
SYS_futex = Constant('SYS_futex',98)
SYS_futimesat = Constant('SYS_futimesat',1066)
SYS_getcpu = Constant('SYS_getcpu',168)
SYS_getcwd = Constant('SYS_getcwd',17)
SYS_getdents = Constant('SYS_getdents',1065)
SYS_getdents64 = Constant('SYS_getdents64',61)
SYS_getegid = Constant('SYS_getegid',177)
SYS_geteuid = Constant('SYS_geteuid',175)
SYS_getgid = Constant('SYS_getgid',176)
SYS_getgroups = Constant('SYS_getgroups',158)
SYS_getitimer = Constant('SYS_getitimer',102)
SYS_get_mempolicy = Constant('SYS_get_mempolicy',236)
SYS_getpeername = Constant('SYS_getpeername',205)
SYS_getpgid = Constant('SYS_getpgid',155)
SYS_getpgrp = Constant('SYS_getpgrp',1060)
SYS_getpid = Constant('SYS_getpid',172)
SYS_getppid = Constant('SYS_getppid',173)
SYS_getpriority = Constant('SYS_getpriority',141)
SYS_getresgid = Constant('SYS_getresgid',150)
SYS_getresuid = Constant('SYS_getresuid',148)
SYS_getrlimit = Constant('SYS_getrlimit',163)
SYS_get_robust_list = Constant('SYS_get_robust_list',100)
SYS_getrusage = Constant('SYS_getrusage',165)
SYS_getsid = Constant('SYS_getsid',156)
SYS_getsockname = Constant('SYS_getsockname',204)
SYS_getsockopt = Constant('SYS_getsockopt',209)
SYS_gettid = Constant('SYS_gettid',178)
SYS_gettimeofday = Constant('SYS_gettimeofday',169)
SYS_getuid = Constant('SYS_getuid',174)
SYS_getxattr = Constant('SYS_getxattr',8)
SYS_init_module = Constant('SYS_init_module',105)
SYS_inotify_add_watch = Constant('SYS_inotify_add_watch',27)
SYS_inotify_init = Constant('SYS_inotify_init',1043)
SYS_inotify_init1 = Constant('SYS_inotify_init1',26)
SYS_inotify_rm_watch = Constant('SYS_inotify_rm_watch',28)
SYS_io_cancel = Constant('SYS_io_cancel',3)
SYS_ioctl = Constant('SYS_ioctl',29)
SYS_io_destroy = Constant('SYS_io_destroy',1)
SYS_io_getevents = Constant('SYS_io_getevents',4)
SYS_ioprio_get = Constant('SYS_ioprio_get',31)
SYS_ioprio_set = Constant('SYS_ioprio_set',30)
SYS_io_setup = Constant('SYS_io_setup',0)
SYS_io_submit = Constant('SYS_io_submit',2)
SYS_kexec_load = Constant('SYS_kexec_load',104)
SYS_keyctl = Constant('SYS_keyctl',219)
SYS_kill = Constant('SYS_kill',129)
SYS_lchown = Constant('SYS_lchown',1032)
SYS_lgetxattr = Constant('SYS_lgetxattr',9)
SYS_link = Constant('SYS_link',1025)
SYS_linkat = Constant('SYS_linkat',37)
SYS_listen = Constant('SYS_listen',201)
SYS_listxattr = Constant('SYS_listxattr',11)
SYS_llistxattr = Constant('SYS_llistxattr',12)
SYS_lookup_dcookie = Constant('SYS_lookup_dcookie',18)
SYS_lremovexattr = Constant('SYS_lremovexattr',15)
SYS_lseek = Constant('SYS_lseek',62)
SYS_lsetxattr = Constant('SYS_lsetxattr',6)
SYS_lstat = Constant('SYS_lstat',1039)
SYS_lstat64 = Constant('SYS_lstat64',1050)
SYS_madvise = Constant('SYS_madvise',233)
SYS_mbind = Constant('SYS_mbind',235)
SYS_migrate_pages = Constant('SYS_migrate_pages',238)
SYS_mincore = Constant('SYS_mincore',232)
SYS_mkdir = Constant('SYS_mkdir',1030)
SYS_mkdirat = Constant('SYS_mkdirat',34)
SYS_mknod = Constant('SYS_mknod',1027)
SYS_mknodat = Constant('SYS_mknodat',33)
SYS_mlock = Constant('SYS_mlock',228)
SYS_mlockall = Constant('SYS_mlockall',230)
SYS_mmap = Constant('SYS_mmap',222)
SYS_mount = Constant('SYS_mount',40)
SYS_move_pages = Constant('SYS_move_pages',239)
SYS_mprotect = Constant('SYS_mprotect',226)
SYS_mq_getsetattr = Constant('SYS_mq_getsetattr',185)
SYS_mq_notify = Constant('SYS_mq_notify',184)
SYS_mq_open = Constant('SYS_mq_open',180)
SYS_mq_timedreceive = Constant('SYS_mq_timedreceive',183)
SYS_mq_timedsend = Constant('SYS_mq_timedsend',182)
SYS_mq_unlink = Constant('SYS_mq_unlink',181)
SYS_mremap = Constant('SYS_mremap',216)
SYS_msgctl = Constant('SYS_msgctl',187)
SYS_msgget = Constant('SYS_msgget',186)
SYS_msgrcv = Constant('SYS_msgrcv',188)
SYS_msgsnd = Constant('SYS_msgsnd',189)
SYS_msync = Constant('SYS_msync',227)
SYS_munlock = Constant('SYS_munlock',229)
SYS_munlockall = Constant('SYS_munlockall',231)
SYS_munmap = Constant('SYS_munmap',215)
SYS_nanosleep = Constant('SYS_nanosleep',101)
SYS_newfstatat = Constant('SYS_newfstatat',1054)
SYS_nfsservctl = Constant('SYS_nfsservctl',42)
SYS_open = Constant('SYS_open',1024)
SYS_openat = Constant('SYS_openat',56)
SYS_pause = Constant('SYS_pause',1061)
SYS_perf_event_open = Constant('SYS_perf_event_open',241)
SYS_personality = Constant('SYS_personality',92)
SYS_pipe = Constant('SYS_pipe',1040)
SYS_pipe2 = Constant('SYS_pipe2',59)
SYS_pivot_root = Constant('SYS_pivot_root',41)
SYS_poll = Constant('SYS_poll',1068)
SYS_ppoll = Constant('SYS_ppoll',73)
SYS_prctl = Constant('SYS_prctl',167)
SYS_pread64 = Constant('SYS_pread64',67)
SYS_preadv = Constant('SYS_preadv',69)
SYS_prlimit64 = Constant('SYS_prlimit64',261)
SYS_pselect6 = Constant('SYS_pselect6',72)
SYS_ptrace = Constant('SYS_ptrace',117)
SYS_pwrite64 = Constant('SYS_pwrite64',68)
SYS_pwritev = Constant('SYS_pwritev',70)
SYS_quotactl = Constant('SYS_quotactl',60)
SYS_read = Constant('SYS_read',63)
SYS_readahead = Constant('SYS_readahead',213)
SYS_readlink = Constant('SYS_readlink',1035)
SYS_readlinkat = Constant('SYS_readlinkat',78)
SYS_readv = Constant('SYS_readv',65)
SYS_reboot = Constant('SYS_reboot',142)
SYS_recv = Constant('SYS_recv',1073)
SYS_recvfrom = Constant('SYS_recvfrom',207)
SYS_recvmmsg = Constant('SYS_recvmmsg',243)
SYS_recvmsg = Constant('SYS_recvmsg',212)
SYS_remap_file_pages = Constant('SYS_remap_file_pages',234)
SYS_removexattr = Constant('SYS_removexattr',14)
SYS_rename = Constant('SYS_rename',1034)
SYS_renameat = Constant('SYS_renameat',38)
SYS_request_key = Constant('SYS_request_key',218)
SYS_restart_syscall = Constant('SYS_restart_syscall',128)
SYS_rmdir = Constant('SYS_rmdir',1031)
SYS_rt_sigaction = Constant('SYS_rt_sigaction',134)
SYS_rt_sigpending = Constant('SYS_rt_sigpending',136)
SYS_rt_sigprocmask = Constant('SYS_rt_sigprocmask',135)
SYS_rt_sigqueueinfo = Constant('SYS_rt_sigqueueinfo',138)
SYS_rt_sigreturn = Constant('SYS_rt_sigreturn',139)
SYS_rt_sigsuspend = Constant('SYS_rt_sigsuspend',133)
SYS_rt_sigtimedwait = Constant('SYS_rt_sigtimedwait',137)
SYS_rt_tgsigqueueinfo = Constant('SYS_rt_tgsigqueueinfo',240)
SYS_sched_getaffinity = Constant('SYS_sched_getaffinity',123)
SYS_sched_getparam = Constant('SYS_sched_getparam',121)
SYS_sched_get_priority_max = Constant('SYS_sched_get_priority_max',125)
SYS_sched_get_priority_min = Constant('SYS_sched_get_priority_min',126)
SYS_sched_getscheduler = Constant('SYS_sched_getscheduler',120)
SYS_sched_rr_get_interval = Constant('SYS_sched_rr_get_interval',127)
SYS_sched_setaffinity = Constant('SYS_sched_setaffinity',122)
SYS_sched_setparam = Constant('SYS_sched_setparam',118)
SYS_sched_setscheduler = Constant('SYS_sched_setscheduler',119)
SYS_sched_yield = Constant('SYS_sched_yield',124)
SYS_select = Constant('SYS_select',1067)
SYS_semctl = Constant('SYS_semctl',191)
SYS_semget = Constant('SYS_semget',190)
SYS_semop = Constant('SYS_semop',193)
SYS_semtimedop = Constant('SYS_semtimedop',192)
SYS_send = Constant('SYS_send',1074)
SYS_sendfile = Constant('SYS_sendfile',71)
SYS_sendfile64 = Constant('SYS_sendfile64',1046)
SYS_sendmsg = Constant('SYS_sendmsg',211)
SYS_sendto = Constant('SYS_sendto',206)
SYS_setdomainname = Constant('SYS_setdomainname',162)
SYS_setfsgid = Constant('SYS_setfsgid',152)
SYS_setfsuid = Constant('SYS_setfsuid',151)
SYS_setgid = Constant('SYS_setgid',144)
SYS_setgroups = Constant('SYS_setgroups',159)
SYS_sethostname = Constant('SYS_sethostname',161)
SYS_setitimer = Constant('SYS_setitimer',103)
SYS_set_mempolicy = Constant('SYS_set_mempolicy',237)
SYS_setpgid = Constant('SYS_setpgid',154)
SYS_setpriority = Constant('SYS_setpriority',140)
SYS_setregid = Constant('SYS_setregid',143)
SYS_setresgid = Constant('SYS_setresgid',149)
SYS_setresuid = Constant('SYS_setresuid',147)
SYS_setreuid = Constant('SYS_setreuid',145)
SYS_setrlimit = Constant('SYS_setrlimit',164)
SYS_set_robust_list = Constant('SYS_set_robust_list',99)
SYS_setsid = Constant('SYS_setsid',157)
SYS_setsockopt = Constant('SYS_setsockopt',208)
SYS_set_tid_address = Constant('SYS_set_tid_address',96)
SYS_settimeofday = Constant('SYS_settimeofday',170)
SYS_setuid = Constant('SYS_setuid',146)
SYS_setxattr = Constant('SYS_setxattr',5)
SYS_shmat = Constant('SYS_shmat',196)
SYS_shmctl = Constant('SYS_shmctl',195)
SYS_shmdt = Constant('SYS_shmdt',197)
SYS_shmget = Constant('SYS_shmget',194)
SYS_shutdown = Constant('SYS_shutdown',210)
SYS_sigaltstack = Constant('SYS_sigaltstack',132)
SYS_signalfd = Constant('SYS_signalfd',1045)
SYS_signalfd4 = Constant('SYS_signalfd4',74)
SYS_sigreturn = Constant('SYS_sigreturn',1999)
SYS_socket = Constant('SYS_socket',198)
SYS_socketpair = Constant('SYS_socketpair',199)
SYS_splice = Constant('SYS_splice',76)
SYS_stat = Constant('SYS_stat',1038)
SYS_stat64 = Constant('SYS_stat64',1049)
SYS_statfs = Constant('SYS_statfs',43)
SYS_statfs64 = Constant('SYS_statfs64',1056)
SYS_swapoff = Constant('SYS_swapoff',225)
SYS_swapon = Constant('SYS_swapon',224)
SYS_symlink = Constant('SYS_symlink',1036)
SYS_symlinkat = Constant('SYS_symlinkat',36)
SYS_sync = Constant('SYS_sync',81)
SYS_sync_file_range2 = Constant('SYS_sync_file_range2',84)
SYS__sysctl = Constant('SYS__sysctl',1078)
SYS_sysinfo = Constant('SYS_sysinfo',179)
SYS_syslog = Constant('SYS_syslog',116)
SYS_tee = Constant('SYS_tee',77)
SYS_tgkill = Constant('SYS_tgkill',131)
SYS_time = Constant('SYS_time',1062)
SYS_timer_create = Constant('SYS_timer_create',107)
SYS_timer_delete = Constant('SYS_timer_delete',111)
SYS_timerfd_create = Constant('SYS_timerfd_create',85)
SYS_timerfd_gettime = Constant('SYS_timerfd_gettime',87)
SYS_timerfd_settime = Constant('SYS_timerfd_settime',86)
SYS_timer_getoverrun = Constant('SYS_timer_getoverrun',109)
SYS_timer_gettime = Constant('SYS_timer_gettime',108)
SYS_timer_settime = Constant('SYS_timer_settime',110)
SYS_times = Constant('SYS_times',153)
SYS_tkill = Constant('SYS_tkill',130)
SYS_truncate = Constant('SYS_truncate',45)
SYS_truncate64 = Constant('SYS_truncate64',1048)
SYS_umask = Constant('SYS_umask',166)
SYS_umount = Constant('SYS_umount',1076)
SYS_umount2 = Constant('SYS_umount2',39)
SYS_uname = Constant('SYS_uname',160)
SYS_unlink = Constant('SYS_unlink',1026)
SYS_unlinkat = Constant('SYS_unlinkat',35)
SYS_unshare = Constant('SYS_unshare',97)
SYS_uselib = Constant('SYS_uselib',1077)
SYS_ustat = Constant('SYS_ustat',1070)
SYS_utime = Constant('SYS_utime',1063)
SYS_utimensat = Constant('SYS_utimensat',88)
SYS_utimes = Constant('SYS_utimes',1037)
SYS_vfork = Constant('SYS_vfork',1071)
SYS_vhangup = Constant('SYS_vhangup',58)
SYS_vmsplice = Constant('SYS_vmsplice',75)
SYS_wait4 = Constant('SYS_wait4',260)
SYS_waitid = Constant('SYS_waitid',95)
SYS_write = Constant('SYS_write',64)
SYS_writev = Constant('SYS_writev',66)
