pragma solidity ^0.4.25;

contract ParentContract {
    modifier parentModifier() {
        _;
    }

    function withOneModifier() internal parentModifier { }

    function parentWithNoModifier() public {}
}
