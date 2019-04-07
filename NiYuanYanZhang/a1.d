import std.bigint;
import std.stdio, std.exception;
import std.algorithm;


int extended_gcd(in int a, in int b, out int x, out int y)
{
    if (b ==0) {
        x = 1, y=0;
        return a;
    } else
    {
        int r = extended_gcd(b, a%b, x, y);
        int temp = x;
        x = y;
        y = temp - a/b*y;
        return r;
    }
}

BigInt extended_gcd(in BigInt a, in BigInt b, out BigInt x, out BigInt y)
{
    if (b ==0) {
        x = 1, y=0;
        return a;
    } else
    {
        BigInt r = extended_gcd(b, a%b, x, y);
        BigInt temp = x;
        x = y;
        y = temp - a/b*y;
        return r;
    }
}


unittest{
    int a=47,b=30,x,y;
    assert(extended_gcd(a,b,x,y) == 1);
    assert(x == -7);
    assert(y == 11);
    writefln("%s = %s * %s +%s * %s", 1, a, x, b, y);

    BigInt A="7145926641669316036254588816301", B="56781982794522489042432639320434378739200", X,Y;
    BigInt r = extended_gcd(A,B,X,Y);
    writefln("%s = %s * %s +%s * %s", r, A, X, B, Y);

}