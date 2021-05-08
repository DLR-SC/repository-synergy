# jniostorlab

## Description

Script to enumerate JNI methods in ELF files. The script identifies statically and dynamically defined JNI methods.
Dynamic JNI methods are heuristically identified using Java method signature particular format.

## Dependencies

The script uses nm to retrieve ELF symbols.

## Usage

```shell
> $ python jniostorlab.py lib/armeabi-v7a/libcj.so
[+] Found method 'Java_com_instagram_creation_jpeg_JpegBridge_calcBWpoint' at 0x285c
[+] Found method 'Java_com_instagram_creation_jpeg_JpegBridge_calcCDF' at 0x2cc4
[+] Found method 'Java_com_instagram_creation_jpeg_JpegBridge_decodeCroppedJpeg' at 0x2b82
[+] Found method 'Java_com_instagram_creation_jpeg_JpegBridge_decodeFullJpeg' at 0x2b7c
[+] Found method 'Java_com_instagram_creation_jpeg_JpegBridge_getJpegLibraryNameNative' at 0x2384
[+] Found method 'Java_com_instagram_creation_jpeg_JpegBridge_getJpegLibraryVersionNative' at 0x2398
[+] Found method 'Java_com_instagram_creation_jpeg_JpegBridge_loadBufferToTexture' at 0x2694
[+] Found method 'Java_com_instagram_creation_jpeg_JpegBridge_loadCDF' at 0x2818
[+] Found method 'Java_com_instagram_creation_jpeg_JpegBridge_readFramebuffer' at 0x2c44
[+] Found method 'Java_com_instagram_creation_jpeg_JpegBridge_releaseNativeBuffer' at 0x28f0
[+] Found method 'Java_com_instagram_creation_jpeg_JpegBridge_rotateImage' at 0x26cc
[+] Found method 'Java_com_instagram_creation_jpeg_JpegBridge_saveImage' at 0x2744
[+] Found method 'Java_com_instagram_creation_jpeg_JpegBridge_saveImageFromGlContext' at 0x256c
[+] Found method 'Java_com_instagram_creation_jpeg_JpegBridge_scaleImage' at 0x2ba0
[+] Found method 'Java_com_instagram_creation_jpeg_JpegBridge_uploadTexture' at 0x27c8
[+] Found method 'Java_com_instagram_creation_photo_bridge_RenderBridge_computeHistogram' at 0x3068
[+] Found method 'Java_com_instagram_creation_photo_bridge_RenderBridge_configureImage' at 0x3050
[+] Found method 'Java_com_instagram_creation_photo_bridge_RenderBridge_mirrorAndComputeHistogram' at 0x30fc
[+] Found method 'Java_com_instagram_creation_photo_bridge_RenderBridge_mirrorImage' at 0x3190
[+] Found method 'Java_com_instagram_creation_photo_bridge_RenderBridge_readRenderResult' at 0x33c4
[+] Found method 'Java_com_instagram_creation_photo_bridge_RenderBridge_saveAndClearCachedImage' at 0x31dc
[+] Found method 'Java_com_instagram_creation_photo_bridge_ShaderBridge_compileProgram' at 0x3470
[+] Found method 'Java_com_instagram_creation_photo_edit_luxfilter_HalideBridge_free' at 0x2320
[+] Found method 'Java_com_instagram_creation_photo_edit_luxfilter_HalideBridge_localLaplacian' at 0x22a4
                                                                                                                                                                                                                    
> $ python jniostorlab.py lib/armeabi-v7a/libcronet.so 
[+] Found method 'nativeInitializeStatistics()V' at 0x26be08
[+] Found method 'nativeEnsureInitialized()V' at 0x26be50
[+] Found method 'nativeCronetInitOnMainThread()V' at 0x26bf20
[+] Found method 'nativeNotifyKeyChainChanged()V' at 0x26d200
[+] Found method 'nativeCreateRequestAdapter(JLjava/lang/String;I)J' at 0x26bcd8
[+] Found method 'nativeCreateRequestAdapter(JLjava/lang/String;I)J' at 0x26bfe8
[+] Found method 'nativeAddHeader(JLjava/lang/String;Ljava/lang/String;)V' at 0x26bce4
[+] Found method 'nativeSetMethod(JLjava/lang/String;)V' at 0x26bcf0
[+] Found method 'nativeEnableChunkedUpload(JLjava/lang/String;)V' at 0x26bd14
[+] Found method 'nativeSetUploadData(JLjava/lang/String;[B)V' at 0x26bcfc
[+] Found method 'nativeSetUploadChannel(JLjava/lang/String;J)V' at 0x26bd08
[+] Found method 'nativeDisableRedirects(J)V' at 0x26bd20
[+] Found method 'nativeStart(J)V' at 0x26bd38
[+] Found method 'nativeCancel(J)V' at 0x26bd44
[+] Found method 'nativeDestroyRequestAdapter(J)V' at 0x26bd50
[+] Found method 'nativeReleaseRequestContextAdapter(J)V' at 0x26bdfc
[+] Found method 'nativeStopNetLog(J)V' at 0x26be2c
[+] Found method 'nativeInitRequestContextOnMainThread(J)V' at 0x26be38
[+] Found method 'nativeOnRewindSucceeded(J)V' at 0x26bfa0
[+] Found method 'nativeDestroyAdapter(J)V' at 0x26bfac
[+] Found method 'nativeDisableCache(J)V' at 0x26c00c
[+] Found method 'nativeStart(J)V' at 0x26c018
[+] Found method 'nativeFollowDeferredRedirect(J)V' at 0x26c024
[+] Found method 'nativeDestroy(J)V' at 0x26c108
[+] Found method 'nativeStopNetLog(J)V' at 0x26c120
[+] Found method 'nativeInitRequestContextOnMainThread(J)V' at 0x26c12c
[+] Found method 'nativeProxySettingsChanged(J)V' at 0x26d754
[+] Found method 'nativeAppendChunk(JLjava/nio/ByteBuffer;IZ)V' at 0x26bd2c
[+] Found method 'nativeGetErrorCode(J)I' at 0x26bd5c
[+] Found method 'nativeGetHttpStatusCode(J)I' at 0x26bd68
[+] Found method 'nativeGetHttpStatusText(J)Ljava/lang/String;' at 0x26bd74
[+] Found method 'nativeGetErrorString(J)Ljava/lang/String;' at 0x26bd80
[+] Found method 'nativeGetContentType(J)Ljava/lang/String;' at 0x26bd8c
[+] Found method 'nativeGetNegotiatedProtocol(J)Ljava/lang/String;' at 0x26bdbc
[+] Found method 'nativeGetHttpStatusText(J)Ljava/lang/String;' at 0x26c048
[+] Found method 'nativeGetNegotiatedProtocol(J)Ljava/lang/String;' at 0x26c054
[+] Found method 'nativeGetProxyServer(J)Ljava/lang/String;' at 0x26c060
[+] Found method 'nativeGetContentLength(J)J' at 0x26bd98
[+] Found method 'nativeGetHeader(JLjava/lang/String;)Ljava/lang/String;' at 0x26bda4
[+] Found method 'nativeGetAllHeaders(JLorg/chromium/net/ChromiumUrlRequest$ResponseHeadersMap;)V' at 0x26bdb0
[+] Found method 'nativeGetWasCached(J)Z' at 0x26bdc8
[+] Found method 'nativeGetWasCached(J)Z' at 0x26c078
[+] Found method 'nativeCreateRequestContextAdapter(Ljava/lang/String;ILjava/lang/String;)J' at 0x26bdf0
[+] Found method 'nativeGetStatisticsJSON(Ljava/lang/String;)Ljava/lang/String;' at 0x26be14
[+] Found method 'nativeGetOrigin(Ljava/lang/String;)Ljava/lang/String;' at 0x26d048
[+] Found method 'nativeGetScheme(Ljava/lang/String;)Ljava/lang/String;' at 0x26d054
[+] Found method 'nativeStartNetLogToFile(JLjava/lang/String;Z)V' at 0x26be20
[+] Found method 'nativeStartNetLogToFile(JLjava/lang/String;Z)V' at 0x26c114
[+] Found method 'nativeGetHistogramDeltas()[B' at 0x26be44
[+] Found method 'nativeCronetInitApplicationContext(Landroid/content/Context;)V' at 0x26bf2c
[+] Found method 'nativeGetCronetVersion()Ljava/lang/String;' at 0x26bf38
[+] Found method 'nativeAttachUploadDataToRequest(JJ)J' at 0x26bf70
[+] Found method 'nativeCreateUploadDataStreamForTesting(JJ)J' at 0x26bf88
[+] Found method 'nativeCreateAdapterForTesting()J' at 0x26bf7c
[+] Found method 'nativeOnReadSucceeded(JIZ)V' at 0x26bf94
[+] Found method 'nativeSetHttpMethod(JLjava/lang/String;)Z' at 0x26bff4
[+] Found method 'nativeAddRequestHeader(JLjava/lang/String;Ljava/lang/String;)Z' at 0x26c000
[+] Found method 'nativeReadData(JLjava/nio/ByteBuffer;II)Z' at 0x26c030
[+] Found method 'nativeDestroy(JZ)V' at 0x26c03c
[+] Found method 'nativeProvideRTTObservations(JZ)V' at 0x26c144
[+] Found method 'nativeProvideThroughputObservations(JZ)V' at 0x26c150
[+] Found method 'nativeGetStatus(JLorg/chromium/net/UrlRequest$StatusListener;)V' at 0x26c06c
[+] Found method 'nativeCreateRequestContextAdapter(Ljava/lang/String;)J' at 0x26c0f0
[+] Found method 'nativeSetMinLogLevel(I)I' at 0x26c0fc
[+] Found method 'nativeEnableNetworkQualityEstimator(JZZ)V' at 0x26c138
[+] Found method 'nativeSetResult(JILjava/lang/String;)V' at 0x26d060
[+] Found method 'nativeRecordCertVerifyCapabilitiesHistogram(Z)V' at 0x26d20c
[+] Found method 'nativeNotifyConnectionTypeChanged(JII)V' at 0x26d0a8
[+] Found method 'nativeNotifyOfNetworkConnect(JII)V' at 0x26d0c0
[+] Found method 'nativeNotifyMaxBandwidthChanged(JD)V' at 0x26d0b4
[+] Found method 'nativeNotifyOfNetworkSoonToDisconnect(JI)V' at 0x26d0cc
[+] Found method 'nativeNotifyOfNetworkDisconnect(JI)V' at 0x26d0d8
[+] Found method 'nativeNotifyUpdateActiveNetworkList(J[I)V' at 0x26d0e4
[+] Found method 'nativeGetMaxBandwidthForConnectionSubtype(I)D' at 0x26d0f0
[+] Found method 'nativeGetApplicationContext()Landroid/content/Context;' at 0x26d218
[+] Found method 'nativeProxySettingsChangedTo(JLjava/lang/String;ILjava/lang/String;[Ljava/lang/String;)V' at 0x26d748
[+] Found method 'nativeDoRunLoopOnce(JJ)V' at 0x26c258
[+] Found method 'nativeInitializeThread(JJ)V' at 0x26c420
[+] Found method 'nativeStopThread(JJ)V' at 0x26c42c
[+] Found method 'nativeReset()V' at 0x26c39c
[+] Found method 'nativeInitialize()V' at 0x26c4ec
[+] Found method 'nativeRegisterEnabledObserver()V' at 0x26c504
[+] Found method 'nativeStartATrace()V' at 0x26c510
[+] Found method 'nativeStopATrace()V' at 0x26c51c
[+] Found method 'nativeBeginToplevel()V' at 0x26c54c
[+] Found method 'nativeEndToplevel()V' at 0x26c558
[+] Found method 'nativeOnBatteryChargingChanged()V' at 0x26c9f8
[+] Found method 'nativeOnMainActivitySuspended()V' at 0x26ca04
[+] Found method 'nativeOnMainActivityResumed()V' at 0x26ca10
[+] Found method 'nativeSaveHistogram(Ljava/lang/String;[JI)V' at 0x26c2b8
[+] Found method 'nativeOnApplicationStateChange(I)V' at 0x26c390
[+] Found method 'nativeOnMemoryPressure(I)V' at 0x26c480
[+] Found method 'nativeGetVersionNumber()Ljava/lang/String;' at 0x26c468
[+] Found method 'nativeGetCoreCount()I' at 0x26c3e4
[+] Found method 'nativeHasSwitch(Ljava/lang/String;)Z' at 0x26c3a8
[+] Found method 'nativeTrialExists(Ljava/lang/String;)Z' at 0x26c408
[+] Found method 'nativeGetSwitchValue(Ljava/lang/String;)Ljava/lang/String;' at 0x26c3b4
[+] Found method 'nativeFindFullName(Ljava/lang/String;)Ljava/lang/String;' at 0x26c3fc
[+] Found method 'nativeAppendSwitch(Ljava/lang/String;)V' at 0x26c3c0
[+] Found method 'nativeRecordUserAction(Ljava/lang/String;)V' at 0x26c4f8
[+] Found method 'nativeAppendSwitchWithValue(Ljava/lang/String;Ljava/lang/String;)V' at 0x26c3cc
[+] Found method 'nativeInstant(Ljava/lang/String;Ljava/lang/String;)V' at 0x26c528
[+] Found method 'nativeBegin(Ljava/lang/String;Ljava/lang/String;)V' at 0x26c534
[+] Found method 'nativeEnd(Ljava/lang/String;Ljava/lang/String;)V' at 0x26c540
[+] Found method 'nativeAppendSwitchesAndArguments([Ljava/lang/String;)V' at 0x26c3d8
[+] Found method 'nativeInitCommandLine([Ljava/lang/String;)V' at 0x26c438
[+] Found method 'nativeGetCpuFeatures()J' at 0x26c3f0
[+] Found method 'nativeWriteFileAtomically(Ljava/lang/String;[B)Z' at 0x26c414
[+] Found method 'nativeLibraryLoaded()Z' at 0x26c444
[+] Found method 'nativeForkAndPrefetchNativeLibrary()Z' at 0x26c474
[+] Found method 'nativeRecordChromiumAndroidLinkerBrowserHistogram(ZZIJ)V' at 0x26c450
[+] Found method 'nativeRegisterChromiumAndroidLinkerRendererHistogram(ZZJ)V' at 0x26c45c
[+] Found method 'nativeOverride(ILjava/lang/String;)V' at 0x26c48c
[+] Found method 'nativeRecordCustomTimesHistogramMilliseconds(Ljava/lang/String;IJJJI)V' at 0x26c498
[+] Found method 'nativeRecordBooleanHistogram(Ljava/lang/String;IZ)V' at 0x26c4a4
[+] Found method 'nativeRecordEnumeratedHistogram(Ljava/lang/String;III)V' at 0x26c4b0
[+] Found method 'nativeRecordCustomCountHistogram(Ljava/lang/String;IIIII)V' at 0x26c4bc
[+] Found method 'nativeRecordLinearCountHistogram(Ljava/lang/String;IIIII)V' at 0x26c4c8
[+] Found method 'nativeRecordSparseHistogram(Ljava/lang/String;II)V' at 0x26c4d4
[+] Found method 'nativeGetHistogramValueCountForTesting(Ljava/lang/String;I)I' at 0x26c4e0
[+] Found method 'nativeStartAsync(Ljava/lang/String;J)V' at 0x26c564
[+] Found method 'nativeFinishAsync(Ljava/lang/String;J)V' at 0x26c570
```


