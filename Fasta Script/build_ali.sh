num=1
path=$(pwd)
cd new_fasta
ls *.fasta > fasta_files.txt
lines=$(wc -l < fasta_files.txt)
sed -i 's/.fasta//g' fasta_files.txt
mv fasta_files.txt $path
cd ..
mkdir alignments
while [ $num -le $lines ]
do
file=$(awk 'NR=='$num' {print}' fasta_files.txt)
pname=$(awk 'NR==1 {print $1}' "$(pwd)/new_fasta/${file}.fasta" )
pname1=$(echo $pname | awk -F'|' '{print $3}' )
echo ">P1;$pname1\nsequence:$pname1:::::::0.00: 0.00" > "$(pwd)/alignments/${file}.ali"
awk 'NF==1 {print}' "new_fasta/${file}.fasta" >> "$(pwd)/alignments/${file}.ali"
sed -i '$ s/$/*/' "$(pwd)/alignments/${file}.ali"
num=`expr $num + 1`
done
rm -rf fasta_files.txt
