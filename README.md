# KTBastion

## Prerequisites

Python >= 3.6

## Install

    cd ~
    git clone https://github.com/ktnoc/ktbastion.git
    cd ktbastion/
    virtualenv venv
    source venv/bin/activate
    python setup.py develop

## How-to : 

### Activate the virtual environment : 

    cd ~/ktbastion
    source venv/bin/activate

### Create a bastion : 

    python bastion.py -clala -plulu
or

     python bastion.py --create lala --password lulu

> **Note:** The bastion will initialize empty.
>  The file will be created in the current dir, with the name *lala* and the password *lulu*


### Add an entry : 

    python bastion.py -dlala -plulu -aentry1 -kfdsfsi,gfdg,gfdgfd,908ffffffff

or 

    python bastion.py --decode lala --password lulu -add entry1 --key fdsfsi,gfdg,gfdgfd,908ffffffff

> **Note:** This command will decode the bastion file *lala* with the password *lulu* and add the entry *entry1* containing keys *fdsfsi,gfdg,gfdgfd,908ffffffff*

### List entries : 

    python bastion.py -dlala -plulu -l

or 

    python bastion.py --decode lala --password lulu --list

### View keys of a specific entry : 

    python bastion.py -dlala -plulu -ventry1

or 

    python bastion.py --decode lala --password lulu --view entry1

> **Note:** This command will decode the bastion file *lala* with the password *lulu* and show *entry1* keys.

Result : 

> (venv) ktnoc@apipriv:~/ktbastion$ python bastion.py -dlala -plulu -ventry1
> **Viewing entry1**
>  ['fdsfsi', 'gfdg', 'gfdgfd', '908ffffffff']

### Remove an entry : 

    python bastion.py -dlala -plulu -rentry1

or 

    python bastion.py --decode lala --password lulu --remove entry1

> **Note:** This command will decode the bastion file *lala* with the password *lulu* and remove *entry1*.

