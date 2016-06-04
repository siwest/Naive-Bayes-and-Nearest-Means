$mean = 0;
$data = shift;
for (my $i = 0; $i<10; $i++) {
	system("python nm.py $data.data $data.trainlabels.$i > nm_out");
	$err[$i] = `perl balancedError.pl $data.labels nm_out`;
	chomp $err[$i];
	$mean+= $err[$i];
}
$mean /= 10;
$sd= 0;
for (my $i = 0; $i < 10; $i++) {
	$sd += ($err[$i] - $mean)**2;
}
$sd /= 10;
$sd = sqrt($sd);
print "Nearest means error = $mean ($sd)\n";

$mean = 0;
for (my $i = 0; $i < 10; $i++) {
	system("python nb.py $data.data $data.trainlabels.$i > nb_out");
	$err[$i] = `perl balancedError.pl $data.labels nb_out`;
	chomp $err[$i];
	$mean += $err[$i];
}
$mean /= 10;
$sd = 0;
for (my $i = 0; $i < 10; $i++) {
	$sd += ($err[$i] - $mean)**2
}
$sd /= 10;
$sd = sqrt($sd);
print "Naive Bayes error = $mean ($sd)\n";
