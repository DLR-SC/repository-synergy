# Requirements

On Ubuntu 14.04.2:

```bash
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install -yq oracle-java7-installer scala git python-virtualenv python-dev unzip
```

```bash
curl -O http://apache.cs.utah.edu/spark/spark-1.3.0/spark-1.3.0.tgz
tar xvf spark-1.3.0.tgz
cd spark-1.3.0/
build/sbt assembly
```

```bash
virtualenv spark_venv
source spark_venv/bin/activate
git clone https://github.com/marklit/recommend.git
cd recommend
pip install -r requirements.txt
```

## Film ratings data

```bash
curl -O http://files.grouplens.org/papers/ml-1m.zip
unzip -j ml-1m.zip "*.dat"
```

# Example outputs

## Training

```bash
$ ../bin/spark-submit recommend.py train ratings.dat
```

```
Ratings:      1,000,209
Users:            6,040
Movies:           3,706

Training:       602,241
Validation:     198,919
Test:           199,049

The best model was trained with:
    Rank:                     12
    Lambda:             0.100000
    Iterations:               20
    RMSE on test set:   0.869235
```

```bash
$ ../bin/spark-submit recommend.py train ratings.dat \
    --ranks=8,9,10 --lambdas=0.31,0.32,0.33 --iterations=3
```

```
The best model was trained with:
    Rank:                     10
    Lambda:             0.320000
    Iterations:                3
    RMSE on test set:   0.931992
```

```bash
$ ../bin/spark-submit recommend.py train ratings.dat \
    --ranks=5,10,15,20 --lambdas=0.33,0.5,0.8,0.9 --iterations=3,6,9
```

```
The best model was trained with:
    Rank:                     15
    Lambda:             0.330000
    Iterations:                3
    RMSE on test set:   0.939317
```

## Recommending

```bash
$ ../bin/spark-submit recommend.py recommend ratings.dat movies.dat
```

```
His Girl Friday (1940)
New Jersey Drive (1995)
Breakfast at Tiffany's (1961)
Halloween 5: The Revenge of Michael Myers (1989)
Just the Ticket (1999)
I'll Be Home For Christmas (1998)
Goya in Bordeaux (Goya en Bodeos) (1999)
For the Moment (1994)
Thomas and the Magic Railroad (2000)
Message in a Bottle (1999)
...
```

```bash
$ ../bin/spark-submit recommend.py recommend ratings.dat movies.dat \
    --rank=15 --lambda=0.33 --iteration=3
```

```
Goya in Bordeaux (Goya en Bodeos) (1999)
Slums of Beverly Hills, The (1998)
New Jersey Drive (1995)
Bottle Rocket (1996)
I'll Be Home For Christmas (1998)
Big Daddy (1999)
Kurt & Courtney (1998)
Kika (1993)
Omega Man, The (1971)
Boogie Nights (1997)
...
```