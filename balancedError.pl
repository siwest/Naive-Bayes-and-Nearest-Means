$true = shift;
open(IN, $true);
while(<IN>) {
	chomp $_;
	@s = split(/\s+/,$_);
	$truelabels{$s[1]} = $s[0];
} close IN;

$predict = shift;
open(IN, $predict);
while(<IN>) {
	chomp $_;
	@s = split(/\s+/,$_);
	if(defined($truelabels{$s[1]})) {
		$predictedlabels{$s[1]} = $s[0];
	}
} close IN;

# for (my $i=0; $i < scalar(@c1); $i++) {
# 	print $c1[$i]."\n";
# }
# foreach my $x (keys %testclass) {
# 	print "$x testclass{$x}\n";
# }
# foreach my $x (keys %trueclass) {
# 	print "$x $trueclass{$x}\n";
# }
# foreach my $x (keys %testclass) {
# 	print "$x $testclass{$x}\n";
# }

$error = 0;
foreach my $x (keys %predictedlabels) {
	if ($truelabels{$x}==0 && $predictedlabels{$x}==0) {
		$a++;
	}
	if ($truelabels{$x}==0 && $predictedlabels{$x}==1) {
		$b++;
	}
	if ($truelabels{$x}==1 && $predictedlabels{$x}==0) {
		$c++;
	}
	if ($truelabels{$x}==1 && $predictedlabels{$x}==1) {
		$d++;
	}
}

# print "a=$a, b=$b, c=$c, d=$d\n";
$BER = 0.5* ($b / ($a+$b) + $c / ($c+$d));
print "$BER";

