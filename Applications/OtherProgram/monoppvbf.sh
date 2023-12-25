energy=("13500" "25000" "37500")
mass=("1000" "2000" "3000" "4000" "5000" "6000" "7000" "8000" "9000" "10000" "11000" "12000" "13000")
for j in {0..2..1}
do
    for i in {0..12..1}
    do
        echo "launch monovbfs" > momoscalarorder
        echo "detector = OFF" >> momoscalarorder
        echo "shower = OFF" >> momoscalarorder
        echo "0" >> momoscalarorder
        echo "set Mmns=${mass[$i]}" >> momoscalarorder
        echo "set gmns=20.746" >> momoscalarorder
        echo "set gmnf=0.0" >> momoscalarorder
        echo "set gmnv=0.0" >> momoscalarorder
        echo "set ebeam1=${energy[$j]}" >> momoscalarorder
        echo "set ebeam2=${energy[$j]}" >> momoscalarorder
        echo "set nevents=10000" >> momoscalarorder
        ./bin/mg5_aMC momoscalarorder
    done
done