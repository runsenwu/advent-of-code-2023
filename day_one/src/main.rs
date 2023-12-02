use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut final_result = 0;
    let mut count = 0;

    if let Ok(lines) = read_lines("./input.txt") {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(ip) = line {
                count += 1;
                final_result += process_two_digit(ip);
            }
        }
    }
    println!("{}", final_result.to_string());
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
    where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn process_two_digit(input: String) -> i32 {
    // first and last digit only;
    let mut first = '0';
    let mut last = '0';

    let mut first_seen = false;

    // process and form two digit
    for c in input.chars() {
        if c.is_numeric() {
            if !first_seen {
                first = c;
                first_seen = true;
                last = c;
            } else {
                last = c;
            }
        }
    }

    let final_number = (first.to_string() + &last.to_string()).parse::<i32>().unwrap();
    return final_number;
}