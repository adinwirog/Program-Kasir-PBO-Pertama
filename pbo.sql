-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 01 Jan 2021 pada 23.44
-- Versi server: 10.4.16-MariaDB
-- Versi PHP: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pbo`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin`
--

CREATE TABLE `admin` (
  `idadmin` int(1) NOT NULL,
  `namaadmin` varchar(8) NOT NULL,
  `usernameadmin` varchar(8) NOT NULL,
  `passwordadmin` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `admin`
--

INSERT INTO `admin` (`idadmin`, `namaadmin`, `usernameadmin`, `passwordadmin`) VALUES
(2, 'Andini', 'ula123', 'kolotero');

-- --------------------------------------------------------

--
-- Struktur dari tabel `operator kasir`
--

CREATE TABLE `operator kasir` (
  `idoperator` int(10) NOT NULL,
  `namaoperator` varchar(25) NOT NULL,
  `nik` varchar(16) NOT NULL,
  `usernamekasir` varchar(8) NOT NULL,
  `passwordkasir` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `operator kasir`
--

INSERT INTO `operator kasir` (`idoperator`, `namaoperator`, `nik`, `usernamekasir`, `passwordkasir`) VALUES
(4, 'Melati Purnamasari', '103456789134', 'melatipr', 'akucanti');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pembeli`
--

CREATE TABLE `pembeli` (
  `idpembeli` int(11) NOT NULL,
  `namapembeli` varchar(20) NOT NULL,
  `telepon` varchar(13) NOT NULL,
  `alamat` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `pembeli`
--

INSERT INTO `pembeli` (`idpembeli`, `namapembeli`, `telepon`, `alamat`) VALUES
(2, 'Ratih', '890234871242', 'Jl. Gangsa RT17 RW 5');

-- --------------------------------------------------------

--
-- Struktur dari tabel `produk`
--

CREATE TABLE `produk` (
  `idbarang` int(4) NOT NULL,
  `namabarang` varchar(20) NOT NULL,
  `hargabarang` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `produk`
--

INSERT INTO `produk` (`idbarang`, `namabarang`, `hargabarang`) VALUES
(1, 'White Jumbo', 2500),
(2, 'White Mini', 1000),
(3, 'Brown Jumbo', 2500),
(4, 'Brown Mini', 1000),
(5, 'Rainbow Jumbo', 2500),
(6, 'Rainbow Ancungan', 2500),
(7, 'Gronong Special', 2500);

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaksi`
--

CREATE TABLE `transaksi` (
  `idtransaksi` int(11) NOT NULL,
  `idoperator` int(10) DEFAULT NULL,
  `idbarang` int(8) NOT NULL,
  `idpembeli` int(11) NOT NULL,
  `kuantitas` int(11) NOT NULL,
  `totalharga` int(11) NOT NULL,
  `tanggaltransaksi` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `transaksi`
--

INSERT INTO `transaksi` (`idtransaksi`, `idoperator`, `idbarang`, `idpembeli`, `kuantitas`, `totalharga`, `tanggaltransaksi`) VALUES
(1, 4, 1, 2, 40, 100000, '2021-01-02 05:31:52'),
(2, 4, 3, 2, 30, 75000, '2021-01-02 05:31:52');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`idadmin`);

--
-- Indeks untuk tabel `operator kasir`
--
ALTER TABLE `operator kasir`
  ADD PRIMARY KEY (`idoperator`);

--
-- Indeks untuk tabel `pembeli`
--
ALTER TABLE `pembeli`
  ADD PRIMARY KEY (`idpembeli`);

--
-- Indeks untuk tabel `produk`
--
ALTER TABLE `produk`
  ADD PRIMARY KEY (`idbarang`);

--
-- Indeks untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`idtransaksi`),
  ADD KEY `idoperator` (`idoperator`),
  ADD KEY `idbarang` (`idbarang`),
  ADD KEY `idpembeli` (`idpembeli`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `admin`
--
ALTER TABLE `admin`
  MODIFY `idadmin` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `operator kasir`
--
ALTER TABLE `operator kasir`
  MODIFY `idoperator` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `pembeli`
--
ALTER TABLE `pembeli`
  MODIFY `idpembeli` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `produk`
--
ALTER TABLE `produk`
  MODIFY `idbarang` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `idtransaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD CONSTRAINT `transaksi_ibfk_3` FOREIGN KEY (`idbarang`) REFERENCES `produk` (`idbarang`),
  ADD CONSTRAINT `transaksi_ibfk_4` FOREIGN KEY (`idoperator`) REFERENCES `operator kasir` (`idoperator`) ON DELETE SET NULL,
  ADD CONSTRAINT `transaksi_ibfk_5` FOREIGN KEY (`idpembeli`) REFERENCES `pembeli` (`idpembeli`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
