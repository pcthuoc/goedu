#include "testlib.h"
#include <bits/stdc++.h>
 
using namespace std;

int check(int t)
{
    while (t--)
    {
        int outp = ouf.readInt();
        int n = inf.readInt();
        int x;
        unordered_map<int, int> m;
        int ok = 0;
        for (int i = 0; i < n; ++i)
        {
            x = inf.readInt();
            m[x] = 1;
        }
        if (ok == 0)
            if (outp != -1)
                return 1;
        if (ok)
            if (m[outp] == 0)
                return 1;
    }
    return 1;
}
 
int main(int argc, char * argv[])
{
    setName("Compare");
    registerTestlibCmd(argc, argv);
    int t = inf.readInt();
    while (t--)
    {
        int n = inf.readInt();
        int x;
        unordered_map<int, int> m;
        int outp = ouf.readInt();
        int res = 0;
        while (n--)
        {
            x = inf.readInt();
            ++m[x];
            res ^= x;
        }
        if (res == 0)
        {
            if (outp == -1 or m[outp] == 0)
                quitf(_wa, "Incorrect! %d", outp);
        }
        else if (outp != -1)
            quitf(_wa, "Incorrect! %d", outp);
    }
    quitf(_ok, "Correct!");
}
