Scripts to track time using ledger and Fava/beancount. Summary of the day's time is provided in the terminal and visualizations of time spent over any period is accomplished through [Fava](https://beancount.github.io/fava/).

**Usage**

Use `ti` and `to` to check into and out of a project. respectively. Projects adapt a heirarchical structure as used in ledger, an accounting program, like so: project:subproject:subsubproject and so on. 

`timelogaccounts` generates a list of all projects that you've ever checked into.

`timelogupdate` parses the timelog file and provides a summary of the amount of time spent in today's projects. It also updates the beancount version of timelog, which can be loaded into [Fava](https://beancount.github.io/fava/) for visualizations.

**Requirements**

bash, ledger, beancount, python3

**Required Environment variables**

$TIMELOG: Ledger file containing checkin and checkout entries from ti/to. File will be created upon first use of `ti`.
$TIMELOGBEANCOUNT: Beancount file containing checkin and checkout entries formatted for Beancount. File will be created.
$TIMELOGACCOUNTS: File containing all projects that you've checked into previously. File wil be created upon first use of `timelogaccounts`
