Run either the uphex.py or uphexunittests.py. These scripts call uphexfunctions.py which contains the forecast, history and a few other needed functions. Please see the dependicies.txt file for the python libraries and versions installed when I ran these. 

Below is a sample calling uphex.py. I haven't been able to find a way to suppress the ConvergenceWarnings's which are a result of the brute force auto arima that had to be developed since Python doesn't have an equivalent of R's auto.arima(). Also, it still prints out the model fits. Not sure if there is a way to suppress that either. Note that I've limited how much I print in the README.txt file.




SAMPLE OUTPUT:
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


329
329
RUNNING THE L-BFGS-B CODE

           * * *

Machine precision = 2.220D-16
 N =            1     M =           12
 This problem is unconstrained.

At X0         0 variables are exactly at the bounds

At iterate    0    f=  5.11212D+00    |proj g|=  0.00000D+00

           * * *

Tit   = total number of iterations
Tnf   = total number of function evaluations
Tnint = total number of segments explored during Cauchy searches
Skip  = number of BFGS updates skipped
Nact  = number of active bounds at final generalized Cauchy point
Projg = norm of the final projected gradient
F     = final function value

           * * *

   N    Tit     Tnf  Tnint  Skip  Nact     Projg        F
    1      0      1      0     0     0   0.000D+00   5.112D+00
  F =   5.1121205034290087     

CONVERGENCE: NORM_OF_PROJECTED_GRADIENT_<=_PGTOL            

 Cauchy                time 0.000E+00 seconds.
 Subspace minimization time 0.000E+00 seconds.
 Line search           time 0.000E+00 seconds.

 Total User time 9.649E-04 seconds.

RUNNING THE L-BFGS-B CODE

           * * *
forecast elements
{'expected_value': [63.71645486632963, 63.61287431854249, 63.50929377075535, 63.40571322296821, 63.30213267518107, 63.19855212739393, 63.09497157960679, 62.99139103181965, 62.887810484032514, 62.784229936245374], 'actual_value': [], 'predictions': [[-6.774103343207628, 134.20701307586688], [-7.7570333437349674, 134.98278198081994], [-8.729259943669632, 135.74784748518033], [-9.691164725284231, 136.50259117122064], [-10.643107123007198, 137.24737247336935], [-11.585426182411275, 137.98253043719913], [-12.518442143563178, 138.70838530277678], [-13.44245786970513, 139.42523993334444], [-14.357760139343497, 140.13338110740852], [-15.264620817374471, 140.83308068986523]], 'point': [330, 331, 332, 333, 334, 335, 336, 337, 338, 339]}
 Total User time 1.718E-01 seconds.

RUNNING THE L-BFGS-B CODE

           * * *

Machine precision = 2.220D-16
 N =            3     M =           12
 This problem is unconstrained.

At X0         0 variables are exactly at the bounds

At iterate    0    f=  5.39876D+00    |proj g|=  1.57208D-03

At iterate    5    f=  5.39876D+00    |proj g|=  4.75708D-04

At iterate   10    f=  5.39875D+00    |proj g|=  4.44089D-06

           * * *

Tit   = total number of iterations
Tnf   = total number of function evaluations
Tnint = total number of segments explored during Cauchy searches
Skip  = number of BFGS updates skipped
Nact  = number of active bounds at final generalized Cauchy point
Projg = norm of the final projected gradient
F     = final function value

           * * *

   N    Tit     Tnf  Tnint  Skip  Nact     Projg        F
    3     13     17      1     0     0   0.000D+00   5.399D+00
  F =   5.3987517363338551     

CONVERGENCE: NORM_OF_PROJECTED_GRADIENT_<=_PGTOL            

 Cauchy                time 0.000E+00 seconds.
 Subspace minimization time 7.915E-05 seconds.
 Line search           time 6.711E-02 seconds.

 Total User time 7.096E-02 seconds.

RUNNING THE L-BFGS-B CODE

           * * *

Machine precision = 2.220D-16
 N =            2     M =           12
 This problem is unconstrained.

At X0         0 variables are exactly at the bounds

At iterate    0    f=  5.00338D+00    |proj g|=  1.18714D-03

At iterate    5    f=  5.00337D+00    |proj g|=  0.00000D+00

           * * *

Tit   = total number of iterations
Tnf   = total number of function evaluations
Tnint = total number of segments explored during Cauchy searches
Skip  = number of BFGS updates skipped
Nact  = number of active bounds at final generalized Cauchy point
Projg = norm of the final projected gradient
F     = final function value

           * * *

   N    Tit     Tnf  Tnint  Skip  Nact     Projg        F
    2      5      7      1     0     0   0.000D+00   5.003D+00
  F =   5.0033688523517839     

CONVERGENCE: NORM_OF_PROJECTED_GRADIENT_<=_PGTOL            

 Cauchy                time 0.000E+00 seconds.
 Subspace minimization time 2.193E-05 seconds.
 Line search           time 2.363E-02 seconds.

 Total User time 2.797E-02 seconds.

RUNNING THE L-BFGS-B CODE

           * * *

Machine precision = 2.220D-16
 N =            1     M =           12
 This problem is unconstrained.

At X0         0 variables are exactly at the bounds

At iterate    0    f=  4.62792D+00    |proj g|=  0.00000D+00

           * * *

Tit   = total number of iterations
Tnf   = total number of function evaluations
Tnint = total number of segments explored during Cauchy searches
Skip  = number of BFGS updates skipped
Nact  = number of active bounds at final generalized Cauchy point
Projg = norm of the final projected gradient
F     = final function value

           * * *

   N    Tit     Tnf  Tnint  Skip  Nact     Projg        F
    1      0      1      0     0     0   0.000D+00   4.628D+00
  F =   4.6279170444087843     

CONVERGENCE: NORM_OF_PROJECTED_GRADIENT_<=_PGTOL            

 Cauchy                time 0.000E+00 seconds.
 Subspace minimization time 0.000E+00 seconds.
 Line search           time 0.000E+00 seconds.

 Total User time 5.341E-04 seconds.


history elements
{'expected_value': [None, None, None, None, 206.0, 383.33333361919733, 120.75, 85.0, 86.33333333333334, -9.0, 75.5, 167.11111111111111, 133.2, 142.46146957594118, 132.02475771914072, 43.58360922161012, 25.57722013319337, 53.58589685570488, 81.32543791287863, 107.89394150343165, 64.59680226763801, 59.12008138989452, 62.793240827767804, 67.54318294294131, 67.45303508738704, 62.462724027024336, 56.25688715063964, 52.086107040846215, 50.45740551505946, 49.75983247150299], 'actual_value': [93.0, 51.0, 45.0, 101.0, 216.0, 169.0, 127.0, 105.0, 49.0, 59.0, 108.0, 118.0, 135.0, 127.0, 73.0, 40.0, 51.0, 75.0, 98.0, 81.0, None, None, None, None, None, None, None, None, None, None], 'predictions': [None, None, None, None, [180.5204682009793, 231.4795317990207], [360.56998342561087, 406.0966838127838], [-62.21751943027439, 303.71751943027436], [-78.72446259128048, 248.72446259128048], [-63.83822662814467, 236.50489329481135], [-150.36995403754275, 132.36995403754275], [-63.89188898594816, 214.89188898594816], [34.17524824465585, 300.0469739775664], [3.82218502795871, 262.57781497204127], [42.840246556153645, 242.0826925957287], [36.321163472577936, 227.7283519657035], [-46.824189699019556, 133.99140814223978], [-61.54169394601174, 112.69613421239848], [-31.408022804131228, 138.57981651554098], [-1.419662199651384, 164.07053802540864], [27.36964145790091, 188.41824154896238], [9.66175934432205, 119.53184519095397], [-13.763889363040121, 132.00405214282915], [-10.432457271467257, 136.01893892700286], [-9.543566474512545, 144.62993236039517], [-13.731727268409486, 148.63779744318356], [-19.022389107081125, 143.9478371611298], [-25.83838889282309, 138.3521631941024], [-31.051802579415593, 135.224016661108], [-32.83888711152399, 133.75369814164293], [-33.62370113581002, 133.143366078816]], 'point': [None, None, None, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}

