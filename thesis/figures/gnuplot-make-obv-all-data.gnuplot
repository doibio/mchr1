set title "Results of all audio feature / machine learning\n runs on the ORCAOBV1 dataset"
set yrange[70:100]
unset key
set ylabel "Accuracy (%)"
set xtics rotate ("FFT Params" 1, "# MFCCs" 2, "LIBLINEAR\nParams" 3, "All\nfeatures" 4, "SVM\Poly" 5, "SVM\nSigmoid" 6, "SVM\nRBF" 7, "Logistic\nRegression" 8, "Naive\nBayes" 9, "Decision\nTree" 10, "Random\nForest" 11, "Multilayer\nPerceptron" 12)
set bmargin at screen 0.2
set output "gnuplot-obv-all-data.ps"
set terminal postscript
plot "gnuplot-obv-all-data.txt", 74.26
