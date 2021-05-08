World Cup results for hackers. Uses Soccer For Good API.

http://softwareforgood.com/soccer-good/

Data Source: http://worldcup.sfg.io/matches

![worldcup.py](http://i.imgur.com/DTUomdM.png)

Note: You can ignore the results on screenshot. I did it by manually :)


### Installing

Just use the pip.

    $ pip install worldcup

### Usage

If you run the `worldcup` directly, fetches and prints all matches.
You can filter matches by time, country or group with custom arguments.

Example 1:
`ENDPOINT` (allowed: 'current' 'today' or 'tomorrow')

    $ worldcup today

     Brazil                         1 - 1                        Croatia
    ------------------------o-------------------------------------------
     ⚽  Being played: 34. minute


     Mexico                         1 - 0                       Cameroon
    --------------------------------------------------------------------
     ⚽  Played 4 days ago. Winner: Mexico


     Spain                          1 - 5                    Netherlands
    --------------------------------------------------------------------
     ⚽  Played 4 days ago. Winner: Netherlands


     Chile                          3 - 1                      Australia
    --------------------------------------------------------------------
     ⚽  Played 4 days ago. Winner: Chile


Example 2:
`-c COUNTRY` or `--country COUNTRY`

    $ worldcup -c bra

      Brazil                         3 - 1                        Croatia
    --------------------------------------------------------------------
    ⚽  Played 10 days ago. Brazil won
    

     Brazil                         0 - 0                         Mexico
    --------------------------------------------------------------------
    ⚽  Played 5 days ago. Draw
    

     Cameroon                       0 - 0                         Brazil
    --------------------------------------------------------------------
    ⚽  Will be played 17 hours from now

Example 3:
`-g GROUP` or `--group GROUP`

    $ worldcup -g 1
    
    Mexico 		| wins: 1 | losses: 0 | goals for: 1 | goals against: 0 | out? False
    --------------------------------------------------------------------
    

    Brazil 		| wins: 1 | losses: 0 | goals for: 3 | goals against: 1 | out? False
    --------------------------------------------------------------------
    

    Croatia 		| wins: 1 | losses: 1 | goals for: 5 | goals against: 3 | out? False
    --------------------------------------------------------------------
    

    Cameroon 		| wins: 0 | losses: 2 | goals for: 0 | goals against: 5 | out? False
    --------------------------------------------------------------------
