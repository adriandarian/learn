#include <stdio.h>
#include <ctype.h> 
#include <string.h>
#define MAXSIZE 4096
int matches_leading(char *partial_line, char *pattern) {
    return 0;
}
int rgrep_matches(char *line, char *pattern) {
    if (*pattern == '\0') {
        return 1;
    }
    int plen = (int) strlen(pattern);
    int llen = (int) strlen(line);
    int additional_iterations = 0;
    int firstpath = 0;
    int secondpath = 0;
    int streak = 0;
    int lpos = 0;
    int offset = 0;
    int degbugvar = 0;
    start:
    for (lpos = 0; lpos < llen; lpos++) {
        if (line[lpos] == '\0') {
            return 0;
        } if (pattern[streak] == '\\') {
            if (pattern[streak + 1] == line[lpos]) { 
                streak++;
            } else {
                streak = 0;
                continue;
            }
        } if (pattern[streak + 1] == '?') {
            if (pattern[streak] == '.') {
                if (additional_iterations == 0) {
                    additional_iterations++;
                } else {
                    additional_iterations = 0;
                } if (firstpath) {
                    goto second;
                } if (secondpath) {
                    goto first;
                }
            } if (line[lpos] == pattern[streak]) {
                first:
                firstpath = 1;
                streak = streak + 2;
                continue;
            } else {
                second:
                secondpath = 1;
                streak = streak + 2;
                lpos = lpos - 1;
                continue;
            }
        } if (pattern[streak + 1] == '+') {
            int i = 0;
            while (1) {
                char recurring = 0;
                if (pattern[streak] == '.') {  
                    recurring = line[lpos];
                } if (degbugvar) {
                    printf("line[lpos + i] = %c\t pattern[streak] = %c\t i = %i\n", line[lpos + i], pattern[streak], i);
                } if (line[lpos + i] == pattern[streak] || line[lpos + i] == recurring) {
                    i++;
                } else if (i != 0){
                    lpos = lpos + i;
                    streak = streak + 2;
                    break;
                } else{
                    break;
                }
            }
            goto ending;
        } if (line[lpos] == pattern[streak] || pattern[streak] == '.') {
            streak++;
        } else {
            streak = 0;
            continue;
        }
        ending:
        if (streak >= plen + offset) {
            return 1;
        }
    }
    if (additional_iterations > 0){
        goto start;
    }
    return 0;
}
int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <PATTERN>\n", argv[0]);
        return 2;
    }
    char buf[MAXSIZE];
    while (!feof(stdin) && !ferror(stdin)) {
        if (!fgets(buf, sizeof(buf), stdin)) {
            break;
        }
        if (rgrep_matches(buf, argv[1])) {
            fputs(buf, stdout);
            fflush(stdout);
        }
    }
    if (ferror(stdin)) {
        perror(argv[0]);
        return 1;
    }
    return 0;
}
