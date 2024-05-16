// Write a program for managing bank accounts. the program should require the user's account number and output the balance and transaction history of the user. Additionally, the user should be allowed to deposit and withdraw

class Account {
    constructor() {
        this.balance = 0;
        this.transactions = []; // Corrected to transactions
        this.accountNumbers = "077654469";
    }

    accountBalance(accountNumber) {
        if (accountNumber === this.accountNumbers) {
            console.log(`Your balance is ${this.balance}`);
        } else {
            console.log(`Red flag`);
        }
    }

    withdraw(amount) {
        if (this.balance >= amount) {
            let wd = this.balance - amount;
            this.balance = wd; 
            this.transactions.push({ type: 'withdrawal', amount }); 
            console.log(`You have withdrawn ${amount} and your balance is now ${this.balance}.`);
        } else {
            console.log(`Insufficient funds.`);
        }
    }

    deposit(amount) {
        let depo = this.balance + amount;
        this.balance = depo; 
        this.transactions.push({ type: 'deposit', amount });
        console.log(`You have deposited ${amount} and your account balance is now ${this.balance}.`);
    }
    checkTransactionHistory() {
        console.log("Transaction History:");
        this.transactions.forEach(transaction => {
            console.log(`${transaction.type}: ${transaction.amount}`);
        });
    }
}

// Usage example
const client = new Account();
client.accountBalance('077654469');
client.withdraw(30000);
client.deposit(40000);
client.checkTransactionHistory();
