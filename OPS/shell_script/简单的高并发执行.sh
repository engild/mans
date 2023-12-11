func_cmd(){
        echo "$i `nova list --all-t --host $i | wc -l`"
}

for i in `cat yfhost`; do
        func_cmd &
        sleep 0.1
done
