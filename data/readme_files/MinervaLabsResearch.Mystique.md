# Mystique
Mystique may be used to discover infection markers that can be used to vaccinate endpoints against malware. It receives as input a malicious sample and automatically generates a list of mutexes that could be used to as “vaccines” against the sample.

# Abstract
It is quite common for malware to mark their territory on the endpoint; leaving a sign to avoid infecting the system more than once. If the malicious program notices this infection marker, it will usually terminate. While malware can implement the marker using many methods, including generating specific files or registry keys, a common approach to marking the machine involves abusing mutex objects. While legitimate processes use mutexes to synchronize access to shared resources on the endpoint, malware can use them to determine whether it is already present on the endpoint.

It’s possible to vaccinate endpoints against infections that involve infection markers by fooling malware into believing that it’s already on the system. However, how could organizations determine whether the specimen relies on infection markers and, what these markers are? This is where Mystique comes in. This open source tool automatically determines the likely mutex-based markers that might be used to immunize endpoints against the malware specimen. Mystique begins by initially executing the user-supplies sample in an analysis sandbox, retrieves the created mutex objects. Then it runs the malware again, this time generating the extracted mutexes, and checks whether generated mutex objects were effective at preventing the sample from executing. Mystique’s output is the list of mutexes that can be used to vaccinate endpoints against the malware.

# Tool details
Mystique may be used to discover infection markers that can be used to vaccinate endpoints against malware. It receives as input a malicious sample and automatically generates a list of mutexes that could be used to as “vaccines” against the sample (if there are any).

The concept implemented by Mystique is not new – academical paper discussing similar framework as a PoC was already released over five years ago by researchers from the FKIE. However, Mystique is an open source tool, fully compatible with the common and easy to use Cuckoo.

Mystique is written in Python and integrates with the Cuckoo Sandbox to “detonate” the user-supplied specimen in a controlled environment to observe active mutex objects and their effects on the malicious program.
After listing the mutex objects that appear after the specimen’s “detonation,” Mystique adjusts the sandbox by generating the likely mutex infection markers and runs the same sample again. Next, Mystique examine the sandbox to determine whether the mutex has changed the sample’s execution flow.

Mystique track’s the specimen’s execution time to determine whether it has decreased dramatically. It also determines whether the number of dropped files or launched processes has changed. Based on the tool’s output the analyst can decide whether the generated mutex can be used as a vaccine, on the basis of those and additional artifacts from Cuckoo’s report, such as number of API calls, the use of exit()after mutex error, and so on. To minimize execution time and to ease the analyst's work, Mystique includes a list of common non-malicious mutex objects. After executing the malware for the first time , it checks the generated mutexes against the whitelist to avoid false positives.

# More about Mystique’s implementation
Cuckoo Sandbox uses the notion of packages to determine what actions should be taken when the sample is executed. When user can chose a specific package when submitting the sample. Cuckoo comes with a set of default packages that help to deal with different file types (.exe, .dll, .py, .doc, and so on). Mystique includes an additional package, which receives one argument as input: mutex name. The package creates the specified mutex before reinfecting the sandbox, so that Mystique can determine whether the mutex has any meaningful effect on the sample’s execution in the sandbox. 

Why name the tool ‘Mystique’? Well, the tool deals with mutants, so an X-Men reference is a must. Mystique is a mutant who can change herself into the person she wants to mimic, not unlike our tool does to mimic the artifacts generated by malware.

# Output example (for CryptoLuck ransomware)

Mystique’s output shows that after the likely infection marker was introduced to the specimen’s runtime environment (the mutex named “CryptoLuck_Instance”), the sample's execution time decreased dramatically, dropping from 139 to 34 seconds. In addition, the output shows that the number of dropped files decreased from 112 to only 4. Moreover, fewer processes were created. This output allows the analyst to confirm that the “CryptoLuck_Instance” mutex can probably be used to vaccinate endpoints against this malware.

# Installation:
Required set up: 
1. Cuckoo Sandbox with a Windows guest machine
2. Python (v2.7). 
2.1 Pymongo.
3. Before running Mystique, the user should copy the Mystique package to Cuckoo’s packages folder. 
4. The user should place the Mystique whitelist file in the same folder where the mystique.py script is located (or give a specific path in the configuration file).
5. Mystique comes with a configuration file. The configuration file must be edited by the user - cuckoo and mongodb ip addresses and ports, VT api key (optional), and output path.
 

# Usage
The user can invoke Mystique in the Cuckoo environment from the command line by executing the mystique.py Python script and specifying the path to the malware sample as the parameter: 

python mystique.py /path/of/file/to/analyze
 
In addition, Mystique developers can import and use in other scripts. For example, the user can create a script that downloads malware from a malware repository and automatically feeds those files to mystique. 

example:
import mystique

for malware in malware_list:
  mystique.main(path\of\sample)