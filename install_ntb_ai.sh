
#!/bin/bash
BASE=/opt/ntb-ai
mkdir -p $BASE
cp -r ntb_core ntb_managers ntb_tools ntb_config ntb_logs $BASE/

echo installing managers...
for d in $BASE/ntb_managers/*; do 
  if [ -x "$d/install.sh" ]; then 
    (cd $d && ./install.sh)
  fi
done
echo done.
