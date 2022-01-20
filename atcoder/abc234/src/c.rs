use proconio::input;

fn main() {
    input! {
        k: usize,
    }

    let mut ok = false;
    let mut b: usize = 1 << 60;
    for _ in 0..61 {
        if k & b > 0 {
            print!("{}", 2);
            ok = true;
        } else if ok {
            print!("{}", 0);
        }
        b >>= 1;
    }
    println!("");
}
