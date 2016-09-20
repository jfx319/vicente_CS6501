



### CS Queues

```bash
jcx9dy@power3
: /if23/jcx9dy ; sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
main*        up   infinite      1 drain* artemis1
main*        up   infinite      4    mix artemis[2-5]
main*        up   infinite      4   idle hermes[1-4]
qdata        up   infinite      1    mix qdata1
qdata        up   infinite      7   idle qdata[2-8]



jcx9dy@power3
: /if23/jcx9dy ; squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
           4845793      main      zsh    xy4cm  R 14-07:42:48      1 artemis3
           4845794      main      zsh    xy4cm  R 14-07:14:05      1 artemis4
           4845795      main      zsh    xy4cm  R 14-07:01:42      1 artemis5
           4845909      main qsub8583 xcg_test  R 11-06:35:52      1 artemis2
           4845928      main qsub6758 xcg_test  R 11-05:21:50      1 artemis2
           4845943      main qsub5688 xcg_test  R 11-04:17:13      1 artemis2
           4845960      main qsub4276 xcg_test  R 11-03:56:08      1 artemis2
           4845976      main qsub2569 xcg_test  R 11-02:33:49      1 artemis2
           4845983      main qsub3454 xcg_test  R 11-01:41:46      1 artemis3
           4845989      main qsub5771 xcg_test  R 11-01:15:41      1 artemis3
           4846001      main qsub4137 xcg_test  R 11-00:01:59      1 artemis3
           4846022      main qsub2105 xcg_test  R 10-21:25:19      1 artemis3
           4846035      main qsub8838 xcg_test  R 10-19:39:46      1 artemis2
           4846037      main qsub2483 xcg_test  R 10-19:11:19      1 artemis2
           4846051      main qsub2805 xcg_test  R 10-17:24:57      1 artemis2
           4846052      main qsub1232 xcg_test  R 10-17:01:56      1 artemis3
           4846054      main qsub3384 xcg_test  R 10-16:52:03      1 artemis2
           4846068      main qsub4052 xcg_test  R 10-14:17:50      1 artemis2
           4846076      main qsub3808 xcg_test  R 10-12:44:33      1 artemis3
           4848972      main qsub3907 xcg_test  R 9-23:31:00      1 artemis2
           4848975      main qsub3483 xcg_test  R 9-22:34:12      1 artemis2
           4848979      main qsub2833 xcg_test  R 9-20:47:29      1 artemis2
           4848981      main qsub5282 xcg_test  R 9-19:03:39      1 artemis2
           4849757      main qsub8598 xcg_test  R 9-04:44:32      1 artemis3
           4849758      main qsub3357 xcg_test  R 8-18:17:53      1 artemis2
           4856295      main qsub2983 xcg_test  R 5-18:20:52      1 artemis4
           4856299      main qsub8838 xcg_test  R 5-18:00:03      1 artemis4
           4856410      main qsub2325 xcg_test  R 5-03:38:42      1 artemis4
           4856424      main qsub2686 xcg_test  R 5-02:16:21      1 artemis5
           4856451      main qsub2730 xcg_test  R 4-22:55:56      1 artemis4
           4856457      main qsub1097 xcg_test  R 4-22:16:55      1 artemis4
           4856605      main qsub1561 xcg_test  R 4-16:21:58      1 artemis3
           4856618      main qsub1904 xcg_test  R 4-14:54:13      1 artemis4
           4856631      main qsub7833 xcg_test  R 4-13:17:52      1 artemis4
           4856645      main qsub4204 xcg_test  R 4-11:05:48      1 artemis4
           4856653      main qsub4774 xcg_test  R 4-09:37:18      1 artemis3
           4856664      main qsub4478 xcg_test  R 4-07:30:56      1 artemis4
           4856720      main qsub2960 xcg_test  R 3-18:37:51      1 artemis3
           4856733      main qsub6339 xcg_test  R 3-15:08:46      1 artemis3
           4856749      main qsub9033 xcg_test  R 3-11:04:31      1 artemis4
           4856769      main qsub6530 xcg_test  R 3-07:24:13      1 artemis3
           4856797      main qsub8062 xcg_test  R 3-02:48:18      1 artemis4
           4856819      main qsub7184 xcg_test  R 2-22:11:11      1 artemis2
           4856842      main qsub1496 xcg_test  R 2-15:49:51      1 artemis4
           4856873      main qsub5331 xcg_test  R 2-08:56:19      1 artemis3
           4856910      main qsub8847 xcg_test  R 1-22:30:44      1 artemis4
           4856917      main qsub3887 xcg_test  R 1-19:09:46      1 artemis4
           4856919      main qsub3649 xcg_test  R 1-18:14:38      1 artemis4
           4856934      main qsub2927 xcg_test  R    4:42:25      1 artemis3
           4789109     qdata     bash    wx4ed  R 108-05:34:07      1 qdata1
           4789110     qdata     bash    wx4ed  R 108-05:32:58      1 qdata1

```



Please start looking for that friend with a powerful gaming machine, or ask for one graphics card for your next birthday, assuming your birthday is soon, or ask your advisor to buy you one. I recommend you ask for this one http://www.geforce.com/hardware/10series/geforce-gtx-1080, it costs $700 (has 8GB of memory) but it is as close as it gets to the Ferrari's of deep learning which are the Pascals Titan X (12GB of memory) that are selling for $1200. I also heard good things about GTX 1070 and GTX 1060, the last which runs at only $250. All you need is an available PCI Express slot in a machine, and for the Pascal Titan X you might also need to upgrade on a better power source. Here is a benchmark by a student at Stanford between GTX 1080 and two versions of the Titan X (Pascal and Maxwell) https://github.com/jcjohnson/cnn-benchmarks/blob/master/README.md  (Maxwell == bad)

Another option is to use the GPU machines our department already has. We have K20's (only 5 though) which are great for 64-bit precision operations but we usually just use FloatTensors for deep learning so this capacity is useless and unfortunately their 32-bit operations are slower than other cheaper cards like the ones mentioned earlier. But they still should run computations much faster than on a CPU. You can check how to use them here: https://www.cs.virginia.edu/~csadmin/wiki/index.php/SLURM. If you are a graduate student in CS you already have access to this cluster and if you are an undergrad you can request such access. If you are in the Data Science program I heard you also have some GPU machines available there but I can't help you much with information about that.

Yet another option is to go to the cloud. Amazon has AWS instances that have GPUs, and as a student you can sign up to their free tier and get some free credits from here https://aws.amazon.com/education/. They gave me $70 for free in computations just by requesting it the other day. You can try that. I have run deep learning models on the GPU on AWS successfully and it is relatively painless once everything is setup. In fact you might get attached to AWS so much you won't feel the need to ever buy a computer anymore. For the people who already have experience with AWS, it is a bit difficult however to get "spot instances" with GPUs but "on demand" you can get for sure. You can see that the on demand price for the g2.2xlarge machine is only $0.65 per hour https://aws.amazon.com/ec2/pricing/ and has a 4GB GPU, and the g2.8xlarge featuring 4 GPUs costs $2.6 an hour.  If you use your free $70 credits, you probably can train the model for your project without having to buy your own GPU (or machine!) as long as it takes less than 70 hours of training. 
 
I also will leave a question with this post for you to think about: Why a graphics card used to play videogames is helpful for training a convolutional neural network so much faster? If you have an answer I want to hear about it next class.

