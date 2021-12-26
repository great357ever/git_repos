#include <bitset>

long flippingBits(long n) {
    std::bitset<32> b = n;
    return b.flip().to_ulong();
}
