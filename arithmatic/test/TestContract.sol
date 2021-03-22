pragma solidity ^0.4.25;

contract TestContract {
    uint a=0;
    uint b=0;
    function addBalance() public { 
        uint c =a+b;
    }

    function deductBalance() public { 
        uint c =a-b;
    }    
    function divideBalance() public { 
        uint c =a/b;
    }
    function MultiplyBalance() public { 
        uint c =a*b;
    }   
    // function obfuscation() public{
    //     string obfp = '+dfdf';
    //     string obf ='-';
    //     string obfd = '/';
    //     string obfm = '*';
    // }
}
