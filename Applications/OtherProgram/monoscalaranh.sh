mass=("1000" "2000" "3000" "4000" "5000" "6000" "7000" "8000" "9000" "10000" "11000" "12000")
for i in {0..11..1}
do
    echo "launch muonmonoscalaranh" > momoscalarorder
    echo "detector = OFF" >> momoscalarorder
    echo "shower = OFF" >> momoscalarorder
    echo "0" >> momoscalarorder
    echo "set Mmns=${mass[$i]}" >> momoscalarorder
    echo "set gmns=20.746" >> momoscalarorder
    echo "set ebeam1=15000" >> momoscalarorder
    echo "set ebeam2=15000" >> momoscalarorder
    echo "set nevents=10000" >> momoscalarorder
    echo "set sde_strategy=1" >> momoscalarorder
    ./bin/mg5_aMC momoscalarorder
done