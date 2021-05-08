# monkey android test
* python3 
* Statistical performance cpu,men,fps,battery,flow(wifi,gprs)
* Statistics crash info.
* muilt android
 


## monkey.ini setting

``` 

cmd=monkey -p com.jianshu.haruki --throttle 500 --ignore-timeouts --ignore-crashes   --monitor-native-crashes -v -v -v 200 >
package_name=com.jianshu.haruki
activity = com.baiji.jianshu.account.SplashScreenActivity
net = wifi 
```

- throttle Each event waits for 500 milliseconds
- net gprs or wifi


![monkey½á¹û](img/analysis.jpg  "monkey½á¹û")

![monkey½á¹û](img/monitor.png  "monkey½á¹û")

![monkey½á¹û](img/crash.PNG  "monkey½á¹û")

# other
* [Chinese](Chinese.md)







