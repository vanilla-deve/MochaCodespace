SAMPLE_CODE = {
    "Python": """#!/usr/bin/env python3
\"\"\"
Simple Python Hello World
\"\"\"

def main():
    print("Hello from Mocha Codespace!")
    print("Python version:", end=" ")
    import sys
    print(sys.version.split()[0])

if __name__ == "__main__":
    main()
""",
    
    "Java": """public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello from Mocha Codespace!");
        System.out.println("Java version: " + System.getProperty("java.version"));
    }
}
""",
    
    "C": """#include <stdio.h>

int main() {
    printf("Hello from  Mocha Codespace!\\n");
    printf("Compiled with C\\n");
    return 0;
}
""",
    
    "C++": """#include <iostream>
#include <string>

int main() {
    std::cout << "Hello from Mocha Codespace!" << std::endl;
    std::cout << "C++ version: " << __cplusplus << std::endl;
    return 0;
}
""",
    
    "JavaScript": """// Hello World in JavaScript
console.log("Hello from Mocha Codespace!");
console.log("Node version:", process.version);

// Example function
function greet(name) {
    return `Hello, ${name}!`;
}

console.log(greet("Developer"));
""",
    
    "TypeScript": """// Hello World in TypeScript
function greet(name: string): string {
    return `Hello, ${name}!`;
}

console.log("Hello from Mocha Codespace!");
console.log(greet("Developer"));

// Example interface
interface Person {
    name: string;
    age: number;
}

const user: Person = {
    name: "Developer",
    age: 25
};

console.log(`User: ${user.name}, Age: ${user.age}`);
""",
    
    "Rust": """// Hello World in Rust
fn main() {
    println!("Hello from Mocha Codespace!");
    println!("Rust is awesome!");
    
    // Example variables
    let name = "Developer";
    let version = "1.0";
    
    println!("Welcome, {}! Version: {}", name, version);
}
""",
    
    "Go": """package main

import (
    "fmt"
    "runtime"
)

func main() {
    fmt.Println("Hello from Mocha Codespace!")
    fmt.Printf("Go version: %s\\n", runtime.Version())
    
    // Example function
    greet("Developer")
}

func greet(name string) {
    fmt.Printf("Hello, %s!\\n", name)
}
""",
    
    "C#": """using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello from Mocha Codespace!");
        Console.WriteLine($"C# version: {Environment.Version}");
        
        // Example method
        string greeting = Greet("Developer");
        Console.WriteLine(greeting);
    }
    
    static string Greet(string name)
    {
        return $"Hello, {name}!";
    }
}
""",
    
    "Ruby": """# Hello World in Ruby
puts "Hello from Mocha Codespace!"
puts "Ruby version: #{RUBY_VERSION}"

# Example method
def greet(name)
  "Hello, #{name}!"
end

puts greet("Developer")

# Example class
class Person
  attr_accessor :name, :age
  
  def initialize(name, age)
    @name = name
    @age = age
  end
  
  def introduce
    "I'm #{@name}, #{@age} years old"
  end
end

person = Person.new("Developer", 25)
puts person.introduce
""",
    
    "Kotlin": """// Hello World in Kotlin
fun main() {
    println("Hello from Mocha Codespace!")
    println("Kotlin is running!")
    
    // Example function
    val greeting = greet("Developer")
    println(greeting)
    
    // Example class
    val person = Person("Developer", 25)
    println(person.introduce())
}

fun greet(name: String): String {
    return "Hello, $name!"
}

class Person(val name: String, val age: Int) {
    fun introduce(): String {
        return "I'm $name, $age years old"
    }
}
""",
    
    "HTML": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello from Mocha Codespace</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }
        h1 {
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello from Mocha Codespace! 🚀</h1>
        <p>Welcome to your HTML page created in Mocha Codespace.</p>
        <p>Edit this file and press Run to see changes in your browser!</p>
    </div>
</body>
</html>
""",
    
    "CSS": """/* Mocha Codespace - Sample Stylesheet */

:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --text-color: #333;
    --bg-color: #f5f5f5;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: var(--bg-color);
    color: var(--text-color);
    line-height: 1.6;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

h1, h2, h3 {
    color: var(--primary-color);
    margin-bottom: 1rem;
}

button {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    transition: transform 0.2s;
}

button:hover {
    transform: scale(1.05);
}
""",
    
    "Lua": """-- Hello World in Lua
print("Hello from Mocha Codespace!")
print("Lua version: " .. _VERSION)

-- Example function
function greet(name)
    return "Hello, " .. name .. "!"
end

print(greet("Developer"))

-- Example table (Lua's main data structure)
local person = {
    name = "Developer",
    age = 25,
    introduce = function(self)
        return "I'm " .. self.name .. ", " .. self.age .. " years old"
    end
}

print(person:introduce())
""",
    
    "Nix": """# Mocha Codespace - Nix Shell Environment
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "mochacode-dev-env";
  
  buildInputs = with pkgs; [
    # Development tools
    gcc
    python3
    nodejs
    
    # Add your dependencies here
  ];
  
  shellHook = ''
    echo "Hello from Mocha Codespace!"
    echo "Nix development environment loaded"
    echo "Available tools: gcc, python3, nodejs"
  '';
}
""",
    "PTX": """
        @P0 IMAD32I.U32.U32 R0, R0, 0x0, R0;
        @P0 FADD32I R0, R0, 0;
        @P0 LD.U8 R0, [R0];
""",
}
