getCGUID = function() {
    function a(a, b) {
        var e = (b || 2) - (1 + Math.floor(Math.log(a | 1) / Math.LN10 + 1E-15));
        return Array(e + 1).join("0") + a
    }
    var b = new Date;
    return "" + a(b.getHours()) + a(b.getMinutes()) + a(b.getSeconds()) + a(b.getMilliseconds(), 3) + a(Math.ceil(9999 * Math.random()), 4)
}

sha1 = function(a) {
    function b(a, b) {
        var c = (a & 65535) + (b & 65535);
        return (a >> 16) + (b >> 16) + (c >> 16) << 16 | c & 65535
    }
    for (var d = [], c = 0; c < 8 * a.length; c += 8)
        d[c >> 5] |= (a.charCodeAt(c / 8) & 255) << 24 - c % 32;
    a = 8 * a.length;
    d[a >> 5] |= 128 << 24 - a % 32;
    d[(a + 64 >> 9 << 4) + 15] = a;
    a = Array(80);
    for (var c = 1732584193, e = -271733879, f = -1732584194, h = 271733878, j = -1009589776, k = 0; k < d.length; k += 16) {
        for (var l = c, m = e, n = f, p = h, q = j, g = 0; 80 > g; g++) {
            a[g] = 16 > g ? d[k + g] : (a[g - 3] ^ a[g - 8] ^ a[g - 14] ^ a[g - 16]) << 1 | (a[g - 3] ^ a[g - 8] ^ a[g - 14] ^ a[g - 16]) >>> 31;
            var r = b(b(c << 5 | c >>> 27, 20 > g ? e & f | ~e & h : 40 > g ? e ^ f ^ h : 60 > g ? e & f | e & h | f & h : e ^ f ^ h), b(b(j, a[g]), 20 > g ? 1518500249 : 40 > g ? 1859775393 : 60 > g ? -1894007588 : -899497514))
              , j = h
              , h = f
              , f = e << 30 | e >>> 2
              , e = c
              , c = r
        }
        c = b(c, l);
        e = b(e, m);
        f = b(f, n);
        h = b(h, p);
        j = b(j, q)
    }
    d = [c, e, f, h, j];
    a = "";
    for (c = 0; c < 4 * d.length; c++)
        a += "0123456789abcdef".charAt(d[c >> 2] >> 8 * (3 - c % 4) + 4 & 15) + "0123456789abcdef".charAt(d[c >> 2] >> 8 * (3 - c % 4) & 15);
    return a
}


check_pd = function(b) {
                function a(a, d) {
                var c = (a & 65535) + (d & 65535);
                return (a >> 16) + (d >> 16) + (c >> 16) << 16 | c & 65535
                                    }
    for (var d = (b.length + 8 >> 6) + 1, c = Array(16 * d), e = 0; e < 16 * d; e++)
        c[e] = 0;
    for (e = 0; e < b.length; e++)
        c[e >> 2] |= b.charCodeAt(e) << 24 - 8 * (e & 3);
    c[e >> 2] |= 128 << 24 - 8 * (e & 3);
    c[16 * d - 1] = 8 * b.length;
    b = Array(80);
    for (var d = 1732584193, e = -271733879, f = -1732584194, h = 271733878, j = -1009589776, k = 0; k < c.length; k += 16) {
        for (var l = d, m = e, n = f, p = h, q = j, g = 0; 80 > g; g++) {
            b[g] = 16 > g ? c[k + g] : (b[g - 3] ^ b[g - 8] ^ b[g - 14] ^ b[g - 16]) << 1 | (b[g - 3] ^ b[g - 8] ^ b[g - 14] ^ b[g - 16]) >>> 31;
            var r = a(a(d << 5 | d >>> 27, 20 > g ? e & f | ~e & h : 40 > g ? e ^ f ^ h : 60 > g ? e & f | e & h | f & h : e ^ f ^ h), a(a(j, b[g]), 20 > g ? 1518500249 : 40 > g ? 1859775393 : 60 > g ? -1894007588 : -899497514))
              , j = h
              , h = f
              , f = e << 30 | e >>> 2
              , e = d
              , d = r
        }
        d = a(d, l);
        e = a(e, m);
        f = a(f, n);
        h = a(h, p);
        j = a(j, q)
    }
    c = [d, e, f, h, j];
    b = "";
    for (d = 0; d < 4 * c.length; d++)
        b += "0123456789abcdef".charAt(c[d >> 2] >> 8 * (3 - d % 4) + 4 & 15) + "0123456789abcdef".charAt(c[d >> 2] >> 8 * (3 - d % 4) & 15);
    return b
}