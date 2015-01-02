Run either the uphex.py or uphexunittests.py. These scripts call uphexfunctions.py which contains the forecast, history and a few other needed functions. Please see the dependicies.txt file for the python libraries and versions installed when I ran these. 

Below is a sample calling uphex.py. I haven't been able to find a way to suppress the ConvergenceWarnings's which are a result of the brute force auto arima that had to be developed since Python doesn't have an equivalent of R's auto.arima().



[cjacobik@ip-172-31-62-16 code]$ python uphex.py > nohup.out
/usr/lib64/python2.7/site-packages/statsmodels-0.6.1-py2.7-linux-x86_64.egg/statsmodels/base/model.py:443: RuntimeWarning: Inverting hessian failed, no bse or cov_params available
  warn(warndoc, RuntimeWarning)
/usr/lib64/python2.7/site-packages/statsmodels-0.6.1-py2.7-linux-x86_64.egg/statsmodels/base/model.py:466: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  "Check mle_retvals", ConvergenceWarning)
/usr/lib64/python2.7/site-packages/statsmodels-0.6.1-py2.7-linux-x86_64.egg/statsmodels/base/model.py:466: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  "Check mle_retvals", ConvergenceWarning)
/usr/lib64/python2.7/site-packages/statsmodels-0.6.1-py2.7-linux-x86_64.egg/statsmodels/base/model.py:466: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  "Check mle_retvals", ConvergenceWarning)
/usr/lib64/python2.7/site-packages/statsmodels-0.6.1-py2.7-linux-x86_64.egg/statsmodels/base/model.py:466: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
  "Check mle_retvals", ConvergenceWarning)



