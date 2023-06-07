<?php
function extractDomain($url) {
    $parsedUrl = parse_url($url);
    $domain = $parsedUrl['host'];

    if (substr($domain, 0, 4) === 'www.') {
        $domain = substr($domain, 4);
    }

    return $domain;
}

// Mengambil input nama file dari pengguna
$handle = fopen("php://stdin", "r");
echo "Masukkan nama file: ";
$fileName = trim(fgets($handle));
fclose($handle);

// Membaca daftar URL dari file
$urls = file($fileName, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

// Mengkonversi setiap URL menjadi domain
$convertedDomains = [];
foreach ($urls as $url) {
    $domain = extractDomain($url);
    $convertedDomains[] = $domain;
}

// Menyimpan hasil konversi ke dalam file
$saveFile = 'ress.txt';
file_put_contents($saveFile, implode("\n", $convertedDomains));

echo "Hasil konversi telah disimpan dalam file $saveFile\n";
?>
