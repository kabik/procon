use proconio::input;

fn main() {
    input! {
        (H, W): (usize, usize),
        (R, C): (usize, usize),
    }

    let mut ans = 0;
    if (C == W || C == 1) && (R == H || R == 1) {
        ans = 2
    } else if R == 1 || R == H || C == 1 || C == W {
        ans = 3
    } else {
        ans = 4
    }

    if H == 1 && W == 1 {
        ans = 0
    } else if H == 1 || W == 1 {
        ans -= 1
    }
    println!("{}", ans)
}
