use proconio::input;

fn main() {
    input! {
        (n, p, q): (usize, usize, usize),
        a: [usize; n],
    }

    let mut ans = 0;
    for i in 0..n-4 {
        for j in i+1..n-3 {
            for k in j+1..n-2 {
                for l in k+1..n-1 {
                    for m in l+1..n {
                        if a[i]*a[j]%p *a[k]%p *a[l]%p *a[m]%p == q { ans += 1 }
                    }
                }
            }
        }
    }
    println!("{}", ans);
}
