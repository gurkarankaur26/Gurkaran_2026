ERROR Function

An error function (or loss function) is a mathematical way to measure how wrong a model's predictions are.
When a model makes predictions, we compare them with the actual values.
The loss function converts that difference into a single number that represents the overall error.

Loss Function = A formula that measures the difference between predicted values and actual values.

Why we need a Loss Function?

Machine learning models learn by minimizing error.

Process:

Input Data → Model → Prediction
                  ↓
          Compare with Actual Value
                  ↓
             Loss Function
                  ↓
            Error (single number)

The model then adjusts its parameters to reduce this error.

So the goal during training is: Minimize the Loss Function

Better Prediction → Smaller Loss
Worse Prediction → Larger Loss

Different ways to compute the loss=> Most important are 1,2 and 3
        1. Mean Absolute Error(MAE)
        2. Mean Squared Error(MSE)
        3. Root Mean Squared Error(RMSE)
        4. Maximum Error(ME)
        5. Sum of Absolute Differences

Method	Idea	                Sensitivity to Large Errors  Formula
MAE	Absolute difference	Low                          MAE = (|e1| + |e2| + |e3| + ... ) / n
MSE	Square difference	High                         MSE = (e1² + e2² + e3² + ... ) / n
RMSE	Square + root	        High                         RMSE = √MSE 

“MSE is more sensitive to large errors”  means:
Large prediction mistakes increase the loss very rapidly.

Comparison: 

MAE: The loss increases proportionally with the error.Every error increases the loss at the same rate. If the error becomes 10 times larger, the loss also becomes about 10 times larger.

MSE: The loss increases very rapidly for large errors because the error is squared. If the error becomes 10 times larger, the loss becomes about 100 times larger.

RMSE: The loss is based on squared errors like MSE, so large errors increase the loss faster, but the final value remains in the same units as the data, making it easier to interpret.

In short,
MAE → Loss increases linearly with error.
MSE → Loss increases very rapidly for large errors.
RMSE → Similar to MSE but expressed in the same units as the data.

Z-score: 

The Z-score (or standardized score) of a data array (). It subtracts the mean of the data from each element and divides by the standard deviation. This normalizes the data to have a mean of 0 and a standard deviation of 1. 
 A result of 0 means the data point is equal to the mean, a positive number means it is above the mean, and a negative number means it is below the mean. 