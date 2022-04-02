use proconio::input;

fn f(a: i128, b: i128) -> i128 {
    return (a+b)*(a*a+b*b)
}

fn main() {
    input! {
        n: i128,
    }

    let ten = 10 as i128;
    let mut x = ten.pow(20);
    for a in 0..ten.pow(6) {
        let mut ng = -1;
        let mut ok = ten.pow(6)+1;
        while ng < ok-1 {
            let mid = (ng+ok)/2;
            if f(a,mid) < n {
                ng = mid
            } else {
                ok = mid
            }
        }
        let b = ok;
        let x1 = f(a,b);
        if x1 < x {
            x = f(a,b);
        }
    }
    println!("{}", x);
}
