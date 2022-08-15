use proconio::input;

fn main() {
    input! {
        n: usize
    }

    let mut ans = 0;
    for i in 1..=n {
        let mut k = i;
        for d in 2.. {
            if d * d > n { break }
            while k % (d*d) == 0 {
                k /= d*d;
            }
        }
        for d in 1.. {
            if k*d*d > n { break }
            ans += 1;
        }
    }
    println!("{}", ans);
}
