ch1 = Scope.Channel1
ch2 = Scope.Channel2
// Execute based on a condition
if(ch1.measure("Peak2Peak")>0.01 && ch2.measure("Peak2Peak")>0.01){
Charge1 = 0;
//Charge2 = 0;
// Define a threshold
threshold = 0.01
// Estimate area under peak, but only for signals above threshold
ch1.data.forEach(function(s){
if(s>threshold){Charge1 += s}})
 // Make data file
 var filem = File("C:/Users/marcu/OneDrive/Documents/GitHub/MekRelLab/gammalab/Na-22-180-grader.csv")
// If it is a new file: write descriptive first line
if(!filem.exist()){
// Write file header for new measurement file
filem.writeLine("This file contains data for detector 20, for source XXX, taken on 08-02-2021")
}
// Append measurements to file
var textm = Charge1
filem.appendLine(textm)
// Increase index parameter
Index++
}