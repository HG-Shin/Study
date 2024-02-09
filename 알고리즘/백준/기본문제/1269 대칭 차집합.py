a, b = map(int, input().split())

set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

sub_a = set_A - set_B
sub_b = set_B - set_A

print(len(sub_a) + len(sub_b))