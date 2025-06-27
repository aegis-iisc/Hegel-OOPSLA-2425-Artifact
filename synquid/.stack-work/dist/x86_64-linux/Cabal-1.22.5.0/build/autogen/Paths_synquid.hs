module Paths_synquid (
    version,
    getBinDir, getLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
catchIO = Exception.catch

version :: Version
version = Version [0,4] []
bindir, libdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/home/ashish/work/purdue/code/git/synquid/.stack-work/install/x86_64-linux/829fd6d2eaf2caa5835af398ac756f3b93cc7aaab38945b516f36c6eabb34467/7.10.3/bin"
libdir     = "/home/ashish/work/purdue/code/git/synquid/.stack-work/install/x86_64-linux/829fd6d2eaf2caa5835af398ac756f3b93cc7aaab38945b516f36c6eabb34467/7.10.3/lib/x86_64-linux-ghc-7.10.3/synquid-0.4-6XQlCZrwL1wLfzjSk5m4wg"
datadir    = "/home/ashish/work/purdue/code/git/synquid/.stack-work/install/x86_64-linux/829fd6d2eaf2caa5835af398ac756f3b93cc7aaab38945b516f36c6eabb34467/7.10.3/share/x86_64-linux-ghc-7.10.3/synquid-0.4"
libexecdir = "/home/ashish/work/purdue/code/git/synquid/.stack-work/install/x86_64-linux/829fd6d2eaf2caa5835af398ac756f3b93cc7aaab38945b516f36c6eabb34467/7.10.3/libexec"
sysconfdir = "/home/ashish/work/purdue/code/git/synquid/.stack-work/install/x86_64-linux/829fd6d2eaf2caa5835af398ac756f3b93cc7aaab38945b516f36c6eabb34467/7.10.3/etc"

getBinDir, getLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "synquid_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "synquid_libdir") (\_ -> return libdir)
getDataDir = catchIO (getEnv "synquid_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "synquid_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "synquid_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
