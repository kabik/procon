use proconio::input;

fn diff(x1: i32, y1: i32, x2: i32, y2: i32) -> f64 {
    return (((x1-x2).pow(2) + (y1-y2).pow(2)) as f64).powf(0.5) as f64;
}

fn main() {
    input! {
        n: i32,
        xys: [(i32, i32); n],
    }
    let mut ans = 0 as f64;
    for i in 0..(n as usize) {
        let (x1, y1) = xys[i];
        for j in i+1..(n as usize) {
            let (x2, y2) = xys[j];
            ans = f64::max(ans, diff(x1,y1,x2,y2));
        }
    }
    println!("{}", ans);
}
