/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    let result = [];

    function backtrack(start, path) {

        if (path.length === 4) {
            if (start === s.length) {
                result.push(path.join('.'));
            }
            return;
        }

        for (let len = 1; len <= 3; len++) {
            if (start + len > s.length) break;

            let part = s.substring(start, start + len);

            if (part.length > 1 && part[0] === '0') continue;

            if (Number(part) > 255) continue;

            path.push(part);
            backtrack(start + len, path);
            path.pop();
        }
    }

    backtrack(0, []);
    return result;
};