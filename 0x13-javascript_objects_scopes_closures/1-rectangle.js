#!/usr/bin/node
module.exports = class Rectangle {
    constructor (w, h) {
	[this.width, this.height] = [w, h];
    }
};
